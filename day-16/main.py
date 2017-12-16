from functools import lru_cache


def reduce_spins(moves):
    moves_wo_spins = []
    spin = 0
    for op, args in moves:
        if op == 'p':
            moves_wo_spins.append((op, args))
        elif op == 's':
            spin = (spin + int(args[0])) % 16
        elif op == 'x':
            a, b = [int(arg) for arg in args]
            a, b = (a - spin) % 16, (b - spin) % 16
            moves_wo_spins.append((op, (a, b)))

    return spin, moves_wo_spins


moves = [(m[0], tuple(m[1:].split('/')))
         for m in open('data.txt', 'r').read().split(',')]

(total_spin, moves) = reduce_spins(moves)


@lru_cache(maxsize=None)
def dance_round(programs):
    programs = list(programs)

    for op, [a, b] in moves:
        if op == 'p':
            a, b = programs.index(a), programs.index(b)
        programs[a], programs[b] = programs[b], programs[a]

    programs = programs[16 - total_spin:] + programs[:16 - total_spin]

    return tuple(programs)


def generate_cycle(programs):
    results = []
    while True:
        programs = dance_round(programs)

        if programs in results:
            return results
        results.append(programs)


programs = tuple(map(chr, range(ord('a'), ord('p') + 1)))
cycle = generate_cycle(programs)

answer_part_1 = ''.join(cycle[0])
answer_part_2 = ''.join(cycle[(1000 ** 3) % len(cycle) - 1])

print(answer_part_1, answer_part_2)
