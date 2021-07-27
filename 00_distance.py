#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
# KHLjhjknjzlbjxnkn;xzkm zl nz/.,/ nmnklz;nk/ lmz,mn jf;ajvnksdnfv
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moscow_lodon = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
mosco_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_lodon
distances['Moscow']['Paris'] = mosco_paris

distances['London'] = {}
distances['London']['Moscow'] = moscow_lodon
distances['London']['Paris'] = london_paris

distances['Paris'] = {}
distances['Paris']['Moscow'] = mosco_paris
distances['Paris']['London'] = london_paris

pprint(distances)