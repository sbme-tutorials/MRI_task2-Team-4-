# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5 import QtWidgets, QtCore
from task2 import Ui_Form

from PyQt5.QtWidgets import QFileDialog, QLabel
from PyQt5.QtGui import QPixmap , QImage
import sys 
#import cv2
import numpy as np
import matplotlib.pyplot as plt


class ApplicationWindow(QtWidgets.QMainWindow):
    global myImg
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.Browse.clicked.connect(self.Browse_clicked)
      
        
    def Browse_clicked (self) :
          # fileName, _filter = QFileDialog.getOpenFileName(self, "Title", "Default File","(*.py)")
          fileName, _ = QFileDialog.getOpenFileName(self," ", "","All Files (*);;Python Files (*.txt)")
          if fileName:
             PD = open("small_phantom.txt", "rt")     #Opening the txt file
             print ('\n Matrix f: \n',PD.read())     #Reading it 
            imgplot = plt.imshow(PD.read())                #ploting the array feh moshkela hnaa
             self.ui.show_phantom(imgplot)
             print('by')
         

            
from __future__ import division
import numpy as np
import cv2
import matplotlib.pyplot as pl
from PIL import Image
def phantom (n = 256, p_type = 'Modified Shepp-Logan', ellipses = None):
        """
         phantom (n = 256, p_type = 'Modified Shepp-Logan', ellipses = None)
        Create a Shepp-Logan or modified Shepp-Logan phantom.
        A phantom is a known object (either real or purely mathematical)
        that is used for testing image reconstruction algorithms.  The
        Shepp-Logan phantom is a popular mathematical model of a cranial
        slice, made up of a set of ellipses.  This allows rigorous
        testing of computed tomography (CT) algorithms as it can be
        analytically transformed with the radon transform (see the
        function `radon').
        Inputs
        ------
        n : The edge length of the square image to be produced.
        p_type : The type of phantom to produce. Either
          "Modified Shepp-Logan" or "Shepp-Logan".  This is overridden
          if `ellipses' is also specified.
        ellipses : Custom set of ellipses to use.  These should be in
          the form
                [[I, a, b, x0, y0, phi],
                 [I, a, b, x0, y0, phi],
                 ...]
          where each row defines an ellipse.
          I : Additive intensity of the ellipse.
          a : Length of the major axis.
          b : Length of the minor axis.
          x0 : Horizontal offset of the centre of the ellipse.
          y0 : Vertical offset of the centre of the ellipse.
          phi : Counterclockwise rotation of the ellipse in degrees,
                measured as the angle between the horizontal axis and
                the ellipse major axis.
          The image bounding box in the algorithm is [-1, -1], [1, 1],
          so the values of a, b, x0, y0 should all be specified with
          respect to this box.
        Output
        ------
        P : A phantom image.
        Usage example
        -------------
          import matplotlib.pyplot as pl
          P = phantom ()
          pl.imshow (P)
        References
        ----------
        Shepp, L. A.; Logan, B. F.; Reconstructing Interior Head Tissue
        from X-Ray Transmissions, IEEE Transactions on Nuclear Science,
        Feb. 1974, p. 232.
        Toft, P.; "The Radon Transform - Theory and Implementation",
        Ph.D. thesis, Department of Mathematical Modelling, Technical
        University of Denmark, June 1996.
        """

        if (ellipses is None):
                ellipses = _select_phantom (p_type)
        elif (np.size (ellipses, 1) != 6):
                raise AssertionError ("Wrong number of columns in user phantom")

        # Blank image
        p = np.zeros ((n, n))

        # Create the pixel grid
        ygrid, xgrid = np.mgrid[-1:1:(1j*n), -1:1:(1j*n)]

        for ellip in ellipses:
                I   = ellip [0]
                a2  = ellip [1]**2
                b2  = ellip [2]**2
                x0  = ellip [3]
                y0  = ellip [4]
                phi = ellip [5] * np.pi / 180  # Rotation angle in radians

                # Create the offset x and y values for the grid
                x = xgrid - x0
                y = ygrid - y0

                cos_p = np.cos (phi)
                sin_p = np.sin (phi)

                # Find the pixels within the ellipse
                locs = (((x * cos_p + y * sin_p)**2) / a2
              + ((y * cos_p - x * sin_p)**2) / b2) <= 1

                # Add the ellipse intensity to those pixels
                p [locs] += I

        return p


def _select_phantom (name):
        if (name.lower () == 'shepp-logan'):
                e = _shepp_logan ()
        elif (name.lower () == 'modified shepp-logan'):
                e = _mod_shepp_logan ()
        else:
                raise ValueError ("Unknown phantom type: %s" % name)

        return e


def _shepp_logan ():
        #  Standard head phantom, taken from Shepp & Logan
        return [[   2,   .69,   .92,    0,      0,   0],
                [-.98, .6624, .8740,    0, -.0184,   0],
                [-.02, .1100, .3100,  .22,      0, -18],
                [-.02, .1600, .4100, -.22,      0,  18],
                [ .01, .2100, .2500,    0,    .35,   0],
                [ .01, .0460, .0460,    0,     .1,   0],
                [ .02, .0460, .0460,    0,    -.1,   0],
                [ .01, .0460, .0230, -.08,  -.605,   0],
                [ .01, .0230, .0230,    0,  -.606,   0],
                [ .01, .0230, .0460,  .06,  -.605,   0]]

def _mod_shepp_logan ():
        #  Modified version of Shepp & Logan's head phantom,
        #  adjusted to improve contrast.  Taken from Toft.
        return [[   1,   .69,   .92,    0,      0,   0],
                [-.80, .6624, .8740,    0, -.0184,   0],
                [-.20, .1100, .3100,  .22,      0, -18],
                [-.20, .1600, .4100, -.22,      0,  18],
                [ .10, .2100, .2500,    0,    .35,   0],
                [ .10, .0460, .0460,    0,     .1,   0],
                [ .10, .0460, .0460,    0,    -.1,   0],
                [ .10, .0460, .0230, -.08,  -.605,   0],
                [ .10, .0230, .0230,    0,  -.606,   0],
                [ .10, .0230, .0460,  .06,  -.605,   0]]
P = phantom ()

pl.imshow (P, cmap='gray')




# ------------------------------------------------------------------------------
#                               For Lena image
# ------------------------------------------------------------------------------

import os
def load_lena():
    try:
        import scipy.misc
        l = scipy.misc.lena()
    except: # lena has been removed from scipy
        fname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/lena.npz")
        f = np.load(fname)
        l = f['data']
        f.close()
    return l.astype(np.float32)
           
    
        
def main():
     app = QtWidgets.QApplication(sys.argv)
     application = ApplicationWindow()
     application.show()
     sys.exit(app.exec_())


if __name__ == "__main__":
    main()        