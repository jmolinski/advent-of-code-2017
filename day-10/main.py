from functools import reduce
import operator as op
from itertools import count


def reverse_sublist(lst, pos, sublen):
    tail, head = max(pos + sublen - 256, 0), min(256, pos + sublen)
    new = list(reversed(lst[pos:head] + lst[:tail]))
    lst[:tail], lst[pos:head] = new[head - pos:], new[:head - pos]


def knot_hash(lengths, rounds=1):
    lst, position = list(range(256)), 0
    for skip_size, length in enumerate(lengths * rounds):
        reverse_sublist(lst, position, length)
        position = (position + length + skip_size) % 256
    return lst


def make_dense_hash(lst):
    hashed = [reduce(op.xor, lst[i: i + 16]) for i in range(0, 256, 16)]
    return ''.join(f'{c:02x}' for c in hashed)


def hash_binary(hash):
    return ''.join(f'{int(c, 16):04b}' for c in hash)


def count_regions(memory):
    regions = 0
    for i, row in memory.items():
        while '1' in row.values():
            hide_group(i, [k for k in row.keys() if row[k] == '1'][0], memory)
            regions += 1
    return regions


def hide_group(x, y, memory):
    memory[x][y] = '0'
    for x_v, y_v in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if memory.get(x + x_v, {}).get(y + y_v, '0') == '1':
            hide_group(x + x_v, y + y_v, memory)


key_string = open('data.txt', 'r').read()

mem_rows = [[ord(c) for c in l] + [17, 31, 73, 47, 23]
            for l in [f'{key_string}-{i}' for i in range(128)]]

mem_rows = [list(hash_binary(make_dense_hash(knot_hash(r, rounds=64))))
            for r in mem_rows]

enumerated_mem_rows = dict(enumerate(dict(enumerate(r)) for r in mem_rows))

answer_part_1 = sum(r.count('1') for r in mem_rows)
answer_part_2 = count_regions(enumerated_mem_rows)

print(answer_part_1, answer_part_2)
