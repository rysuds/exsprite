import matplotlib.pyplot as plt
from skimage import io, data, filters

def centroid(t1,t2):
    return (int(sum(t1)/2), int(sum(t2)/2))

# Todo refactor to check set of sets for largest then retrieve row
def unique(array, ignore=[0]):
    ignore = set(ignore)
    seen = set()
    u = []
    for a in array:
        if a not in seen and a not in ignore:
            seen.add(a)
            u.append(a)
    return u

def scale_down(img, scalar):
    dims = img.shape
    height, length = dims[0], dims[1]
    return (length/scalar, height/scalar)

def show(img, scalar=1):
    if scalar:
        plt.figure(figsize = scale_down(img, scalar))
    else:
        plt.figure()
    io.imshow(img, aspect='auto')
    io.show()

def filter_bounds(bounds):
    bound_nums, p1 = [], 0
    for p2 in range(1,len(bounds)):
        if bounds[p2]-1 == bounds[p2-1]:
            p2 += 1
        else:
            p1 = p2-1
            bound_nums.append((bounds[p1],bounds[p2]))
    return bound_nums

def get_bounds(int_img):
    return [i for i, row in enumerate(int_img) if not sum(row)]