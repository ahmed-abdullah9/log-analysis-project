#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from analyze import get_posts, request_error, popular_authoer
file = open('result.txt', 'w')

for row in get_posts():
    path = row[0]
    count = row[1]

    file.write(str(path))
    file.write(' — ' + str(count) + " views " + '\n')

file.write('\n')

for row in popular_authoer():
    name = row[0]
    count = row[1]

    file.write(str(name))
    file.write(' — ' + str(count) + ' ' + '\n')

file.write('\n')

for row in request_error():
    date = row[0]
    count = row[1]

    file.write(str(date))
    file.write(' — ' + str(count) + '% errors ' + '\n')

file.close()
