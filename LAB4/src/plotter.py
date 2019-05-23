import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from itertools import cycle
# import numpy as np
# import matplotlib.cm as cm
# from PIL import Image, ImageDraw, ImageColor


def draw_clustering(clustering):
    img = mpimg.imread('inputFiles/USA_Counties.png')

    # img = Image.open('inputFiles/USA_Counties.png').convert('RGB')
    # colors = cycle(['b','g','r','c','m','y','k'])
    # colors = cm.rainbow(np.linspace(0, 1, len(clustering)))
    colors = cycle(['#800000', '#9A6324', '#469990', '#000075', '#000000', 
               '#e6194B', '#f58231', '#ffe119', '#3cb44b', '#42d4f4',
               '#4363d8', '#911eb4', '#f032e6', '#8e8e8e', '#fabebe', 
               '#e6beff'])

    for c in clustering:
        # for county in c.dataset:
        #     colore = ImageColor.getrgb(col)
        #     ImageDraw.floodfill(img, county.get_coords(), colore)
        
        # draw a point over each county of a cluster
        x, y = c.get_coords()
        plt.scatter(x, y, marker='.', linewidth=1.5, c=next(colors))
        # draw lines to the center
        xc, yc = c.get_center()
        for xp, yp in zip(x,y):
            plt.plot([xc,xp], [yc,yp], c='black', linewidth=0.25)

    plt.imshow(img)
    plt.show() 