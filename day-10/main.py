from functools import reduce
import operator as op

raw_lenghts = open('data.txt', 'r').read()
lengths_p1 = [int(l) for l in raw_lenghts.split(',')]
lengths_p2 = [ord(l) for l in raw_lenghts] + [17, 31, 73, 47, 23]


def reverse_sublist(lst, pos, sublen):
    tail, head = max(pos + sublen - 256, 0), min(256, pos + sublen)
    new = list(reversed(lst[pos:head] + lst[:tail]))
    lst[:tail], lst[pos:head] = new[head - pos:], new[:head - pos]


def run_hash(lengths, rounds=1):
    lst, position = list(range(256)), 0
    for skip_size, length in enumerate(lengths * rounds):
        reverse_sublist(lst, position, length)
        position = (position + length + skip_size) % 256
    return lst


def make_dense_hash(lst):
    hashed = [reduce(op.xor, lst[i: i + 16]) for i in range(0, 256, 16)]
    return ''.join(f'{c:02x}' for c in hashed)


answer_part_1 = (lambda st, nd, *_: st * nd)(*run_hash(lengths_p1))
answer_part_2 = make_dense_hash(run_hash(lengths_p2, rounds=64))

print(answer_part_1, answer_part_2)
