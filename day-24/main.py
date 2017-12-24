from collections import Counter
from itertools import chain
from types import GeneratorType


def build_subtree(port, multiset):
    if not multiset:
        yield []
    else:
        matching_parts = [ports for ports in multiset if port in ports]
        for p in matching_parts:
            multiset_cpy = multiset[:]
            multiset_cpy.remove(p)
            yield [p] + list(build_subtree(p[0] if p[1] == port else p[1], multiset_cpy))


def evaluate_possible_paths(so_far, rest):
    this, *tail = rest

    yield so_far + (this,)

    for t in tail:
        yield evaluate_possible_paths(so_far + (this,), t)


def recursive_generator_eval(v, paths):
    if isinstance(v, GeneratorType):
        for y in v:
            recursive_generator_eval(y, paths)
    else:
        paths.append(v)


def flatten(p):
    print('xd')
    if isinstance(p, list):
        yield from [flatten(x) for x in p]
    else:
        yield p


def path_strength(p):
    return sum(a + b for a, b in p)


parts = list(sorted((lambda x, y: tuple(sorted((int(x), int(y)))))(*r.split('/'))
                    for r in open('data.txt', 'r').readlines()))

paths_graph = {}
starting_nodes = [ports for ports in parts if 0 in ports]
paths_possibilities = []
for p in starting_nodes:
    available_parts = parts[:]
    available_parts.remove(p)
    paths_possibilities.append(
        [p] + list(build_subtree(p[1], available_parts)))

paths = tuple(evaluate_possible_paths((), p)
              for p in paths_possibilities)

final_all_paths = []
for starting_path in paths:
    recursive_generator_eval(starting_path, final_all_paths)

longest_bridge_length = len(max(final_all_paths, key=lambda x: len(x)))
longest_bridges = [
    b for b in final_all_paths
    if len(b) == longest_bridge_length
]

answer_part_1 = max(path_strength(p) for p in final_all_paths)
answer_part_2 = max(path_strength(p) for p in longest_bridges)

print(answer_part_1, answer_part_2)
