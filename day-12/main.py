nodes = [(lambda i, _, *children: {int(c.replace(',', '')) for c in children})
         (*row.split()) for row in open('data.txt', 'r').readlines()]


def graph(visited, to_visit, vts):
    if not to_visit:
        return vts
    n = to_visit.pop()
    return graph(visited | {n}, to_visit | nodes[n] - visited, vts | nodes[n])


answer_part_1 = len(graph(set(), {0}, set()))
answer_part_2 = len(set(
    tuple(sorted(graph(set(), {i}, set()))) for i in range(len(nodes))
))

print(answer_part_1, answer_part_2)
