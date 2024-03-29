import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from itertools import cycle


def draw_clustering(clustering, title: str):
    img = mpimg.imread('inputFiles/USA_Counties.png')

    colors = cycle(['#800000', '#9A6324', '#469990', '#0000ad', '#c0be42',
                    '#e6194B', '#f58231', '#ffe119', '#3cb44b', '#42d4f4',
                    '#4363d8', '#911eb4', '#f032e6', '#8e8e8e', '#fabebe',
                    '#e6beff'])

    for c in clustering:
        # draw a point over each county of a cluster
        x, y = c.get_coords()
        plt.scatter(x, y, marker='.', linewidth=1.5, c=next(colors))
        # draw lines to the center
        xc, yc = c.get_center()
        for xp, yp in zip(x, y):
            plt.plot([xc, xp], [yc, yp], c='black', linewidth=0.25)

    plt.title(title)
    plt.imshow(img)
    plt.show()


def draw_distortion(xlist: list, distortion_h: list, distortion_k: list, title: str):
    plt.plot(xlist, distortion_h, label="Hierarchical")
    plt.plot(xlist, distortion_k, label="K-means")
    plt.xlabel("Numero di clusters")
    plt.ylabel("Distorsione")
    plt.title("Distorsione " + title)
    plt.legend()
    plt.show()
