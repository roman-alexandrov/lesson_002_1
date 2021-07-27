#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .slit() нельзя.
# Запятая не должна выводиться.

chart_films = [
    my_favorite_movies[0: 10],
    my_favorite_movies[-16: -1] + my_favorite_movies[-1],
    my_favorite_movies[12: 25],
    my_favorite_movies[-23: -17],
              ]


print(chart_films)