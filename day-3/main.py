from itertools import chain, islice, product
from collections import defaultdict

square = int(open('data.txt', 'r').read())

E, N, W, S = (1, 0), (0, 1), (-1, 0), (0, -1)
vectors = chain.from_iterable(  # vector = coords change from square x to x+1
    sum(([d] * r for d, r in zip((E, N, W, S), (i, i, i + 1, i + 1))), [])
    for i in range(1, square, 2)
)

spiral = [(None, None)]  # list of coords, i -> (x, y)
inverted_spiral = defaultdict(int)  # (x, y) -> value


def neighbours_sum(x, y):
    return sum(inverted_spiral[x + d_x, y + d_y]
               for (d_x), (d_y) in product([-1, 0, 1], repeat=2))


x, y = 0, 0  # pointer vector
first_value_to_exceed = 0
for vec_x, vec_y in islice(vectors, square):
    spiral.append((x, y))
    if square >= first_value_to_exceed:
        first_value_to_exceed = max(1, neighbours_sum(x, y))
        inverted_spiral[(x, y)] = first_value_to_exceed
    x, y = x + vec_x, y + vec_y  # vector addition


answer_part_1 = sum(abs(coord) for coord in spiral[square])
answer_part_2 = first_value_to_exceed

print(answer_part_1, answer_part_2)
