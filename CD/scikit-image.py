from skimage import feature, io
# from memory_profiler import profile
#
#
# @profile(precision=4)
def process():
    image = io.imread('test.png', as_gray=True)
    edge = feature.canny(image)
    return image, edge


img, edges = process()

# io.imsave('ski.png', edges)

