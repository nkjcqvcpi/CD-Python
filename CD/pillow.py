from PIL import Image
import numpy as np
# from memory_profiler import profile
#
#
# @profile(precision=4)
def process():
    img = Image.open('gray.png')
    max_g = 0
    threshold = 0
    n_img = np.asarray(img)
    for th in range(0, 256, 1):
        bin_img = n_img > th
        bin_img_inv = n_img <= th
        fore_pix = np.sum(bin_img)
        back_pix = np.sum(bin_img_inv)
        if 0 == fore_pix:
            break
        if 0 == back_pix:
            continue
        w0 = float(fore_pix) / n_img.size
        u0 = float(np.sum(n_img * bin_img)) / fore_pix
        w1 = float(back_pix) / n_img.size
        u1 = float(np.sum(n_img * bin_img_inv)) / back_pix
        g = w0 * w1 * (u0 - u1) ** 2
        if g > max_g:
            max_g = g
            threshold = th
    table = [0 if i < threshold else 1 for i in range(256)]
    bin_img = img.point(table, '1')
    return img, bin_img


image, o_bin = process()

# o_bin.save("pillow.png")
