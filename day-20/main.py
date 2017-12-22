from collections import namedtuple
from itertools import chain, count
from collections import Counter

Particle = namedtuple('Particle', 'i x y z x_v y_v z_v x_a y_a z_a')

particles = [
    [[int(v) for v in x[3:-1].split(',')]
     for x in line.replace('\n', '').split(', ')]
    for line in open('data.txt', 'r').readlines()
]
particles = [Particle(i, *chain.from_iterable(v))
             for i, v in enumerate(particles)]


def simulate_move(particles, r=1):
    for _ in range(r):
        particles = [
            Particle(p.i,
                     p.x + p.x_v + p.x_a, p.y + p.y_v + p.y_a, p.z + p.z_v + p.z_a,
                     p.x_v + p.x_a, p.y_v + p.y_a, p.z_v + p.z_a,
                     p.x_a, p.y_a, p.z_a,)
            for p in particles
        ]
    return particles


def get_longrun_closest(particles):
    acc_magn = [(abs(p.x_a) + abs(p.y_a) + abs(p.z_a), p) for p in particles]
    acc_magn = sorted(acc_magn, key=lambda x: x[0])
    lowest_acc = [p for acc, p in acc_magn if acc == acc_magn[0][0]]
    longrun_closest = simulate_move(lowest_acc, r=100)

    return min(longrun_closest, key=lambda p: (abs(p.x_v) + abs(p.y_v) + abs(p.z_v)))


def calculate_not_colliding(particles):
    for _ in range(100):
        s = Counter((p.x, p.y, p.z) for p in particles)
        colliding = [coords for coords, p in s.items() if p > 1]
        particles = [p for p in particles if (p.x, p.y, p.z) not in colliding]
        particles = simulate_move(particles)

    return len(particles)


answer_part_1 = get_longrun_closest(particles[:]).i
answer_part_2 = calculate_not_colliding(particles[:])

print(answer_part_1, answer_part_2)
