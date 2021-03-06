import numpy as np
from skimage import data
import ImagePlotter
import Image
import matplotlib.pyplot as plt
import PolygonCreator
import matplotlib.artist as artst
from matplotlib.patches import Polygon

im = Image.Image(np.ma.masked_array(data.camera()), calibration=3)
im.SaveImgAsPNG('/home/isobel/Documents/McMaster/PythonCodes/DataAnalysis/Image_camera.png', [0, 255], cmap=plt.get_cmap('RdBu'))

fig = plt.figure()
ax = plt.axes([0,0,1,1])
implot = ImagePlotter.ImagePlotter(im, ax, cmap=plt.get_cmap('RdBu'))
#creator = PolygonCreator.PolygonCreator(ax)

plt.show()
#im.SaveImgAsPNG('/home/isobel/Documents/McMaster/PythonCodes/DataAnalysis/testIm.png', im.Imglim)
#im2 = Image.Image(im.data*implot.mask)
#fig2 = plt.figure()
#ax2 = plt.axes([0,0,1,1])
#implot2 = ImagePlotter.ImagePlotter(im2, ax2)
#plt.show()
