from PIL import Image
import math
import operator
import glob
import os
import sys
import functools

EXTS = 'jpg', 'jpeg', 'JPG', 'JPEG', 'gif', 'GIF', 'png', 'PNG'


def pil_image_similarity(filepath1, filepath2):


    image1 = Image.open(filepath1)
    image2 = Image.open(filepath2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    rms = math.sqrt(functools.reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return rms
if __name__ == '__main__':
    wd = "./"
    im = "fish5.jpg"
    seq = []

    os.chdir(wd)
    images = []
    for ext in EXTS:
        images.extend(glob.glob('*.%s' % ext))

    prog = int(len(images) > 50 and sys.stdout.isatty())
    for f in images:
        seq.append((f, pil_image_similarity(im, f)))

        if prog:
            perc = 100. * prog / len(images)
            x = int(2 * perc / 5)
            print('\rCalculating... [' + '#' * x + ' ' * (40 - x) + ']',)
            print('%.2f%%' % perc, '(%d/%d)' % (prog, len(images)),)
            sys.stdout.flush()
            prog += 1
    if prog: print

    for f, ham in sorted(seq, key=lambda i: i[1]):
        print("%d\t%s" % (ham, f))

