import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
import numpy as np
# from PIL import Image, ImageDraw, ImageColor

from clustering import center

from county import *

def draw_clustering(clustering):
    img = mpimg.imread('inputFiles/USA_Counties.png')
    # img = Image.open('inputFiles/USA_Counties.png').convert('RGB')

    # colors = cm.rainbow(np.linspace(0, 1, len(clustering)))
    # 16 colori
    colors = ['#800000', '#9A6324', '#469990', '#000075', '#000000', 
              '#e6194B', '#f58231', '#ffe119', '#3cb44b', '#42d4f4',
              '#4363d8', '#911eb4', '#f032e6', '#8e8e8e', '#fabebe', 
              '#e6beff']
    for c, col in zip(clustering, colors):
        """
        for county in c.dataset:
            colore = ImageColor.getrgb(col)
            ImageDraw.floodfill(img, county.get_coords(), colore)
        
        """
        x, y = c.get_coords()
        plt.scatter(x, y, marker='.', c=col)

        xc, yc = center(c)
        for xp, yp in zip(x,y):
            plt.plot([xc,xp], [yc,yp], c='black', linewidth=0.25)

    plt.imshow(img)
    plt.show() 