import itertools
from collections import Counter

with open('data.txt', 'r') as f:
    nodes = [(lambda name, w, *sub: (name, int(w[1:-1]), [n.replace(',', '') for n in sub[1:]]))(*row.split())
             for row in f.readlines()]


tree = {}
for (name, weight, children) in nodes:
    tree[name] = (weight, children, tree.get(name, (0, [], None))[2])
    for child in children:
        tree[child] = tree.get(child, (0, [], None))[:2] + (name,)

answer_part_1 = [name for (name, node) in tree.items() if node[2] is None][0]
answer_part_2 = None

print(answer_part_1, answer_part_2)
