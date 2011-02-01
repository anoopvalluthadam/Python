"""
Little image processing program
It uses Python PIL, Psyco and select modules
by leonardo maffi, V.1.0, Feb 13 2008
"""

from random import choice
from colorsys import rgb_to_yiq
import Image # Python PIL
from select import median # my libs, see my site
import psyco; psyco.full()

class InImage:
    def __init__(self, filename):
        self.inim = Image.open(filename)
        self.nx,self.ny = self.inim.size
        self.inmat = self.inim.load()
    def __getitem__(self, (x, y)):
        return self.inmat[x % self.nx, y % self.ny]
    def all_coords(self):
        for y in xrange(self.ny):
            for x in xrange(self.nx):
                yield x, y
    def neigh(self, x, y, lenx=3, leny=3):
        assert lenx & 1 and leny & 1
        for posy in xrange(-leny/2+1, leny/2+1):
            for posx in xrange(-lenx/2+1, lenx/2+1):
                yield self[x+posx, y+posy]
    def neigh33(self, x, y):
        return [self[x-1, y-1], self[x, y-1], self[x+1, y-1],
                self[x-1, y],   self[x, y],   self[x+1, y],
                self[x-1, y+1], self[x, y+1], self[x+1, y+1]]

class OutImage:
    def __init__(self, in_image):
        self.nx,self.ny = in_image.nx, in_image.ny
        self.outim = in_image.inim.copy()
        self.outmat = self.outim.load()
    def __setitem__(self, (x, y), value):
        self.outmat[x % self.nx, y % self.ny] = value
    def save(self, filename, *args, **kwds):
        self.outim.save(filename, *args, **kwds)

def luminance((r,g,b)):
    return rgb_to_yiq(r/255.0, g/255.0, b/255.0)[0]

def main():
    m1 = InImage("face_part.jpg")
    m2 = OutImage(m1)
    K = 0.8

    lastPixel = (0, 0, 0)
    for x,y in m1.all_coords():
        #m2[x,y] = sorted(m1.neigh33(x, y), key=luminance)[4] # 3x3 median
        #m2[x,y] = max(m1.neigh33(x, y), key=luminance) # 3x3 max
        #m2[x,y] = min(m1.neigh33(x, y), key=luminance) # 3x3 min
        if luminance(m1[x, y]) < K:
            lastPixel = m1[x, y]
        else:
            nonwhite = [(luminance(p), p) for p in m1.neigh33(x, y) if luminance(p) < K]
            if nonwhite:
                lastPixel = median(nonwhite)[1]
            m2[x,y] = lastPixel

    m2.save("face_part_elab.jpg", quality=99)

main()


"""
/// fast median among 9 items
pixelvalue median9(pixelvalue* p) {
    // Formula from: XILINX XCELL magazine, vol. 23 by John L. Smith

    #ifdef PIX_SWAP
    raise some compile-time error here, PIX_SWAP already defined
    #endif
    #define PIX_SWAP(a,b) { pixelvalue temp=(a);(a)=(b);(b)=temp; }

    #ifdef PIX_SORT
    raise some compile-time error here, PIX_SORT already defined
    #endif
    #define PIX_SORT(a,b) { if ((a)>(b)) PIX_SWAP((a),(b)); }

    PIX_SORT(p[1], p[2]); PIX_SORT(p[4], p[5]); PIX_SORT(p[7], p[8]);
    PIX_SORT(p[0], p[1]); PIX_SORT(p[3], p[4]); PIX_SORT(p[6], p[7]);
    PIX_SORT(p[1], p[2]); PIX_SORT(p[4], p[5]); PIX_SORT(p[7], p[8]);
    PIX_SORT(p[0], p[3]); PIX_SORT(p[5], p[8]); PIX_SORT(p[4], p[7]);
    PIX_SORT(p[3], p[6]); PIX_SORT(p[1], p[4]); PIX_SORT(p[2], p[5]);
    PIX_SORT(p[4], p[7]); PIX_SORT(p[4], p[2]); PIX_SORT(p[6], p[4]);
    PIX_SORT(p[4], p[2]);

    #undef PIX_SWAP
    #undef PIX_SORT

    return(p[4]);
}
"""