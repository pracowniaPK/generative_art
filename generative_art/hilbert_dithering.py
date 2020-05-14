from hilbertcurve.hilbertcurve import HilbertCurve
from PIL import Image, ImageDraw

from math import log2, ceil


def hilbert_dithering(im_in, verbose=True):
    im_out = im_in.copy()
    im_width, im_height = im_out.size
    if im_out.mode in ('RGB', 'RGBA'):
        ch = 3
    if im_out.mode in ('L', 'LA'):
        ch = 1
    if verbose:
        print('picture size:', im_width, im_height)
        print('channels:', ch)
    p = ceil(log2(max(im_width, im_height)))
    n = 2
    h = HilbertCurve(p, n) 
    err = [0] * ch
    for i in range(2**(p*n)-1):
    # for i in range(500):
        coords = h.coordinates_from_distance(i)
        if coords[0] < im_width and coords[1] < im_height:
            new_pixel = [0] * ch + [255]
            for j in range(ch):
                current_v = im_out.getpixel(tuple(coords))[j]
                if current_v + err[j] < + 255/2:
                    new_v = 0
                else:
                    new_v = 255
                new_pixel[j] = new_v
                err[j] += current_v - new_v
            new_pixel = tuple(new_pixel)
            im_out.putpixel(coords, new_pixel)
    return im_out



if __name__ == "__main__":    
    filename = 'p2.png'
    im_in = Image.open('img_in/' + filename).convert('LA')
    im_out = hilbert_dithering(im_in)
    im_out.save('img_out/hilbert/' + filename)
    # im_out.show()

