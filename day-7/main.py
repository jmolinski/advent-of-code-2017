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


def subtree_weight(root):
    return tree[root][0] + sum(subtree_weight(child) for child in tree[root][1])


def all_subtrees_have_equal_weights(root):
    weights = [subtree_weight(c) for c in tree[root][1]]
    return len(weights) == 0 or len(weights) == weights.count(weights[0])


def find_wrong_node_correct_weight(root):
    root_level_weights = (subtree_weight(c) for c in tree[root][1])
    (right, _), *_, (wrong, _) = Counter(root_level_weights).most_common()
    wrong_subtree = [c for c in tree[root][1] if subtree_weight(c) == wrong][0]

    if not all_subtrees_have_equal_weights(wrong_subtree):
        return find_wrong_node_correct_weight(wrong_subtree)
    return right - sum(subtree_weight(c) for c in tree[wrong_subtree][1])


answer_part_1 = [name for (name, node) in tree.items() if node[2] is None][0]
answer_part_2 = find_wrong_node_correct_weight(answer_part_1)

print(answer_part_1, answer_part_2)
