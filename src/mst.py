#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "esemi"

from collections import deque

import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial.distance import pdist

from shared import get_data


def graph_draw(g):
    """Draw graph"""

    plt.figure()
    nx.draw_graphviz(g, with_labels=False, node_size=3, prog='neato')


def graph_mst(dist, labels, limit):
    """Обёртка над алгоритмом MST"""

    s = nx.Graph()  # исходный граф
    s.add_nodes_from(labels)
    r = s.copy()  # результат кластеризации

    dq = deque(dist)
    len_x = len(labels)
    for x in xrange(len_x - 1):
        for y in xrange(x + 1, len_x):
            s.add_edge(labels[x], labels[y], weight=dq.popleft())

    mst = nx.minimum_spanning_tree(s)
    plt.hist([edge[2]['weight'] for edge in mst.edges_iter(data=True)], 100, color='red', alpha=0.3)

    edges = [edge for edge in mst.edges_iter(data=True) if edge[2]['weight'] <= limit]
    r.add_edges_from(edges)
    del s

    return mst, r

if __name__ == '__main__':
    names, data = get_data()

    dist = pdist(data, 'euclidean')

    mst, g = graph_mst(dist, names, 0.05)

    graph_draw(mst)
    graph_draw(g)

    plt.show()


