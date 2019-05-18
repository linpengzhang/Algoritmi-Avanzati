import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from county import *

def draw_clustering(C):
    img = mpimg.imread('inputFiles/USA_Counties.png')
    plt.imshow(img)

    plt.show()