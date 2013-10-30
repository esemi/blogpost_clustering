#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'esemi'

def get_data():
    """Возвращает списки идентификаторов объектов и матрицу значений"""
    source = [row.strip().split(';') for row in file('products.csv')]
    names = [row[0].decode('UTF-8') for row in source[1:]]
    data = [map(float, row[1:]) for row in source[1:]]
    return names, data