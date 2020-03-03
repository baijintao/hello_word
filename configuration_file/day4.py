#!/usr/bin/env python
# -*- coding:utf-8 -*-

i = 5
while i >= 1:
    j = 1
    while j <= i:
        print("* ", end='')
        j += 1
    print("\n")
    i -= 1

i = 9
while i >= 1:
    j = 1
    while j <= i:
        print("%d*%d=%-2d " % (j, i, j * i), end='')
        j += 1
    print("\n")
    i -= 1

i = 0
while i < 10:
    i += 1
    print('-----')
    if i == 5:
        break
    print(i)

i = "aStr"
# print(i[3], end='')
# print(i[2], end='')
# print(i[1], end='')
# print(i[0], end='')
print(i[3:1:-1])
