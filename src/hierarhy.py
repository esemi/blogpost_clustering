#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "esemi"

from scipy.spatial.distance import pdist
from scipy.cluster import hierarchy
import sys


def get_data():
    """Возвращает списки идентификаторов объектов и матрицу значений"""
    source = [row.strip().split(';') for row in file('products.csv')]
    names = [row[0].decode('UTF-8') for row in source[1:]]
    data = [map(float, row[1:]) for row in source[1:]]
    return names, data


def hierarchy_draw(Z, labels, level):
    """Рисуем дендрограмму и сохраняем её"""
    import matplotlib.pyplot as plt
    plt.figure()
    hierarchy.dendrogram(Z, labels=labels, color_threshold=level, leaf_font_size=5, count_sort=True)
    plt.show()

if __name__ == '__main__':
    sys.setrecursionlimit(10000)

    names, data = get_data()
    dist = pdist(data, 'euclidean')
    Z = hierarchy.linkage(dist, method='average')
    hierarchy_draw(Z, names, 4.)