from itertools import accumulate
import operator as op

steps = open('data.txt', 'r').read().split(',')

directions = {'n': (0, 2), 's': (0, -2), 'nw': (-1, 1),
              'ne': (1, 1), 'sw': (-1, -1), 'se': (1, -1)}

distances = [  # distances to (0, 0) in consecutive steps
    abs(x) + (max(0, abs(y) - abs(x))) // 2
    for x, y in
    accumulate((directions[d] for d in steps),
               lambda v1, v2: list(map(op.add, v1, v2)))
]

answer_part_1 = distances[-1]
answer_part_2 = max(distances)

print(answer_part_1, answer_part_2)
