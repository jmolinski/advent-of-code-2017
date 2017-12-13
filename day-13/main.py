from itertools import count

layers = dict(r.split(':') for r in open('data.txt').readlines())

layers_num = 1 + max(int(k) for k in layers.keys())
layers = [int(layers.get(str(i), 0)) for i in range(layers_num)]


def step_severity(step, range_len):
    if (step / (range_len - 1)) % 2 == 0:
        return step * range_len
    return 0


def calculate_severity(delay):
    return sum(step_severity(r, r_len)
               for r, r_len in enumerate(layers, start=delay))


def gets_detected(delay):
    return any(step_severity(r, r_len) != 0
               for r, r_len in enumerate(layers, start=delay))


answer_part_1 = calculate_severity(delay=0)
answer_part_2 = next(i for i in count() if not gets_detected(delay=i))

print(answer_part_1, answer_part_2)
