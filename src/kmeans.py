#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "esemi"

from collections import deque

import numpy
from scipy.cluster import *
from scipy.spatial.distance import cdist
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from shared import get_data


def kmeans_export(centroids, data, labels):
    """Export kmeans result"""

    res = [[] for i in xrange(len(centroids))]
    d = cdist(numpy.array(data), centroids, 'euclidean')
    for i, l in enumerate(d):
        res[l.tolist().index(l.min())].append((labels[i], data[i]))

    return res


def kmeans_draw(clusters):
    """Drawing kmeans clustering result"""

    colors = deque(['r', 'g', 'b', 'c', 'm', 'y', 'k'])
    fig = plt.figure()

    # Prior to version 1.0.0, the method of creating a 3D axes was different. For those using older versions of matplotlib,
    # change ax = fig.add_subplot(111, projection='3d') to ax = Axes3D(fig).
    ax = Axes3D(fig)
    for cluster in clusters:
        color = colors.popleft()
        for name, coord in cluster:
            x, y, z = coord
            ax.plot3D([x], [y], [z], marker='o', c=color)

    ax.set_xlabel(u'Белки')
    ax.set_ylabel(u'Жиры')
    ax.set_zlabel(u'Углеводы')
    plt.show()


if __name__ == '__main__':
    names, data = get_data()

    centroids = vq.kmeans(numpy.array(data), 5, iter=200)[0]
    K_res = kmeans_export(centroids, data, names)

    kmeans_draw(K_res)




