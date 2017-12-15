from itertools import islice


def generator(value, factor, cond=lambda x: True):
    while 1:
        value *= factor
        value %= 2147483647
        if cond(value):
            yield value


a_start, b_start = [int(v) for v in open('data.txt', 'r').readline().split()]

generators = zip(generator(a_start, 16807), generator(b_start, 48271))
generators_w_conds = zip(generator(a_start, 16807, lambda x: not x & 3),
                         generator(b_start, 48271, lambda x: not x & 7))

answer_part_1 = sum((a & ((1 << 16) - 1)) == (b & ((1 << 16) - 1))
                    for a, b in islice(generators, 40 * 1000 * 1000))
answer_part_2 = sum((a & ((1 << 16) - 1)) == (b & ((1 << 16) - 1))
                    for a, b in islice(generators_w_conds, 5 * 1000 * 1000))

print(answer_part_1, answer_part_2)
