import os
import math
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, data, filters
from skimage.viewer import ImageViewer
from skimage.exposure import histogram
from skimage.measure import label
from skimage.segmentation import flood, flood_fill
from scipy import ndimage
from scipy.ndimage.measurements import label
from PIL import Image
import cv2

# https://www.youtube.com/watch?v=TyWtx7q2D7Y
# Connected componenets

def scale_down(img, scalar):
    dims = img.shape
    height, length = dims[0], dims[1]
    return (length/scalar, height/scalar)

def show(img, scalar=1):
    if scalar:
        fig = plt.figure(figsize = scale_down(img, scalar))
    else:
        fig = plt.figure()
    io.imshow(img, aspect='auto')
    io.show()

def centroid(t1,t2):
    return (int(sum(t1)/2), int(sum(t2)/2))

def read_img(filename):
    """
        Function that returns image and integer background
    """
    img = io.imread(filename)
    return img

def get_integer_background(img, bcolor=0):
    background = flood(img[..., 0], (0,0), tolerance=0.0)
    img[background] = bcolor
    intback = np.invert(background).astype(int)
    return intback

img = read_img('link.png')
intback = get_integer_background(img)
structure = np.ones((3, 3), dtype=np.int)
labeled, ncomponents = label(intback, structure)
clusters = []
for n in range(ncomponents):
    raw_inds = np.where(labeled==n)
    rrow, rcol = raw_inds
#     indices = zip(rrow, rcol)
#     indices = sorted(indices, key=lambda x:x[1])
#     indices = sorted(indices, key=lambda x:x[0])
#     least_index = indices[0]
    minr, maxr = int(min(rrow)), int(max(rrow))
    minc, maxc = int(min(rcol)), int(max(rcol))
    least_index = (maxr,maxc)
    comp_dict = {
        'index': n,
        'row_tup': (minr, maxr+1),
        'col_tup': (minc, maxc+1),
        'sort_point': least_index
    }
    #comp_dict['point'] = centroid((minr, maxr+1),(minc, maxc+1))
    #comp_dict['point'] = least_index
    #comp_dict['img'] = img[minr:maxr+1,minc:maxc+1]
    #sub_image = img[minr:maxr+1,minc:maxc+1]
    #show(sub_image,50)
    clusters.append(comp_dict)
    
    
clusters = sorted(clusters, key=lambda k: k['sort_point'][1]) 
clusters = sorted(clusters, key=lambda k: k['sort_point'][0]) 




### POST SORT LOGIC ####
#print(len(clusters))
for c in clusters[0:20]:
#for sort_n in component_sort_dict:
    #c = clusters[sort_n]
    #print(c['index'], c['point'])
    topleft, topright = c['row_tup']
    botleft, botright = c['col_tup']
    sub_image = img[topleft:topright,botleft:botright]
    #io.imsave(f'tmp/img{n}.png',sub_image)
#     print(c['point'])
    show(sub_image,50)
        

##### Sub Div stuff ######
# def get_diff_list(rows):
#     diffrows = [None]
#     for i in range(len(rows)-1):
#         if rows[i+1]-rows[i] ==1:
#             continue
#         else:
#             if diffrows[-1]!=rows[i]:
#                 diffrows.append(rows[i])
#             diffrows.append(rows[i+1])
#     return diffrows[1:]
    
# rows = []
# for row in range(len(img)):
#     num_colors = len(set(list(tuple(x) for x in img[row])))
#     if num_colors == 1:
#         rows.append(row)
# print(rows)

# diffrows = get_diff_list(rows)
# col_dict = {}
# for i in range(len(diffrows)-1):
#     up, down = diffrows[i],diffrows[i+1]
#     for col in range(len(img[0])):
#         num_colors = len(set(list(tuple(x) for x in img[up:down,col])))
#         if num_colors == 1:
#             if (up,down) not in col_dict:
#                 col_dict[(up,down)] = []
#             col_dict[(up,down)].append(col)
    
# for rbound in rows:
#     img[rbound,:] = 255
    
# for tup,col in col_dict.items():
#     up,down = tup
#     img[up:down,col] = 255

# row_dict = {}
# for tup in col_dict:
#     up,down = tup
#     bound_cols = get_diff_list(col_dict[tup])
#     for i in range(len(bound_cols)-1):
#         left,right = bound_cols[i], bound_cols[i+1]
#         for row in range(up,down+1):
#             num_colors = len(set(list(tuple(x) for x in img[row,left:right])))
#             if num_colors == 1:
#                 if row not in row_dict:
#                     row_dict[row] = []
#                 row_dict[row] = (left,right)
#                 #img[row,left:right] = 0

# for row,tup in row_dict.items():
#     left,right = tup
#     img[row,left:right] = 255
# show(img,50)




