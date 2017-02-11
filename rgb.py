import cv2.cv as cv
import os
import glob
import sys
EXTS = 'jpg', 'jpeg', 'JPG', 'JPEG', 'gif', 'GIF', 'png', 'PNG'

def createHist(img):
    #cv.CvtColor(img,img,cv.CV_BGR2HSV)
    b_plane = cv.CreateImage((img.width,img.height), 8, 1)
    g_plane = cv.CreateImage((img.width,img.height), 8, 1)
    r_plane = cv.CreateImage((img.width,img.height), 8, 1)


    cv.Split(img,b_plane,g_plane,r_plane,None)
    planes = [b_plane, g_plane, r_plane]

    bins = 4
    b_bins = bins
    g_bins = bins
    r_bins = bins

    hist_size = [b_bins,g_bins,r_bins]
    b_range = [0,255]
    g_range = [0,255]
    r_range = [0,255]

    ranges = [b_range,g_range,r_range]
    hist = cv.CreateHist(hist_size, cv.CV_HIST_ARRAY, ranges, 1)
    cv.CalcHist([cv.GetImage(i) for i in planes], hist)
    cv.NormalizeHist(hist,1)
    return hist

def imgcompare(image1,image2):
    img1 = cv.LoadImage(image1)
    hist1 = createHist(img1)
    img2 = cv.LoadImage(image2)
    hist2 = createHist(img2)
    return cv.CompareHist(hist1,hist2,cv.CV_COMP_CORREL)

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
        seq.append((f, imgcompare(im, f)))

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