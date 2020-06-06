import os
import math
import numpy as np
from skimage import io
from skimage.exposure import histogram
from skimage.measure import label
from skimage.segmentation import flood, flood_fill
from scipy import ndimage
from scipy.ndimage.measurements import label
from functools import reduce
from PIL import Image
import cv2
import fire
from exsprite.utils import show, unique, filter_bounds, get_bounds


def get_chunk(tup, labeled):
    i, j = tup
    return [unique(r) for r in labeled[i+1:j]]

def get_chunk_set(chunk):
    chunk_sets = list(map(set, chunk))
    return reduce(lambda a,b: a.union(b), chunk_sets)


def get_labeled_for_rows(labeled, row_tups):
    sprite_rows = []
    for tup in row_tups:
        max_row = []
        chunk = get_chunk(tup, labeled)
        chunk_set = get_chunk_set(chunk)
        sorted_rows = sorted(chunk, key=lambda x: len(x), reverse=True)
        if not sorted_rows:
            continue
        while set(max_row) != chunk_set:
            extra = sorted_rows.pop(0)
            max_row.extend(extra)
        sprite_rows.append(unique(max_row))
    return sprite_rows


class SpriteSheet(object):
    def __init__(self, filename, background=0):
        self.filename = filename
        self.foldername = f"{filename.split('.')[0]}_groups"
        self.img = io.imread(filename)
        self.background=background
        self.boolean_image=None
        self.num_labels=None
        self.labeled_image=None
        self._get_boolean_image()
        self._get_labeled_image()

    def _get_boolean_image(self):
        background = flood(self.img[..., 0], (0,0), tolerance=0.0)
        self.img[background] = 0
        self.boolean_image = np.invert(background).astype(int)

    def _get_labeled_image(self):
        structure = np.ones((3, 3), dtype=np.int)
        labeled, ncomponents = label(self.boolean_image, structure)
        self.labeled_image = labeled
        self.num_labels = ncomponents

    def _get_sprite_groups(self):
        print(self.boolean_image)
        bound_tups = filter_bounds(get_bounds(self.boolean_image))
        sprite_groups = get_labeled_for_rows(self.labeled_image, bound_tups)
        return sprite_groups

    #TODO allow for custom foldernames
    def _check_create_folder(self,foldername=None):
        foldername = foldername if foldername else self.foldername
        if foldername not in set(os.listdir()):
            os.mkdir(foldername)
        return foldername

    def save(self):
        sprite_groups = self._get_sprite_groups()
        self._check_create_folder()
        for group_num, group in enumerate(sprite_groups):
            group_foldername = f"{self.foldername}/group_{group_num}"
            self._check_create_folder(group_foldername)
            for i, label in enumerate(group):
                filename = f"{group_foldername}/g{group_num}_{i}.png"
                raw_inds = np.where(self.labeled_image==label)
                rrow, rcol = raw_inds
                minr, maxr = int(min(rrow)), int(max(rrow))
                minc, maxc = int(min(rcol)), int(max(rcol))
                sub_image = self.img[minr:maxr+1,minc:maxc+1]
                #show(sub_image,50)
                io.imsave(filename,sub_image)
