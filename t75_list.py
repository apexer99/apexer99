# -*- coding: utf-8 -*-
#import os.path


def solution1(mylist):
    answer = sum(mylist, [])
    return answer


x1 = [[1], [2]]
x2 = [['A', 'B'], ['X','Y'], ['1']]

print(solution1(x1))
print(solution1(x2))

import itertools

def solution2(mylist):
    answer = list(map(list, itertools.permutations(mylist)))
    answer.sort()
    return answer

y2 = [2, 1]
y3 = [1, 2, 3]
y4 = [1, 2, 3, 4]
#y5 = [1, 2, 3, 4, 5]
print(solution2(y2))
print(solution2(y3))
print(solution2(y4))
#print(solution2(y5))

iterable1 = "ABCD"
iterable2 = "xy"
iterable3 = "1234"
print(list(itertools.product(iterable1, iterable2, iterable3)))



import hashlib

str1 = "이름"
str2 = "생일7월28일"

result = hashlib.sha256(str1.encode())
print(result.hexdigest())

result = hashlib.sha256(str2.encode())
print(result.hexdigest())