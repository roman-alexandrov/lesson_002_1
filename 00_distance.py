#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
# привет от Акима
sites = {
    'Moscow': (550, 370),
    'Armavir': (510, 510),
    'Krasnodar': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()

moscow = sites['Moscow']
london = sites['Armavir']
paris = sites['Krasnodar']

moscow_lodon = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
mosco_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5

distances['Moscow'] = {}
distances['Moscow']['Armavir'] = moscow_lodon
distances['Moscow']['Krasnodar'] = mosco_paris

distances['Armavir'] = {}
distances['Armavir']['Moscow'] = moscow_lodon
distances['Armavir']['Krasnodar'] = london_paris

distances['Krasnodar'] = {}
distances['Krasnodar']['Moscow'] = mosco_paris
distances['Krasnodar']['Armavir'] = london_paris

pprint(distances)

constant = 0.0167
speed_priora = 110

minuty_moscow_lodon = 0
clock_moscow_lodon = 0
a = 0
while a < 1:
    if moscow_lodon < speed_priora:
        minuty_moscow_lodon = moscow_lodon / (speed_priora * constant)
        a = 1
    else:
        clock_moscow_lodon = clock_moscow_lodon + 1
        moscow_lodon = moscow_lodon - speed_priora

print('От Москвы до Армавира ехать ', clock_moscow_lodon,' час ', minuty_moscow_lodon, ' минут')




