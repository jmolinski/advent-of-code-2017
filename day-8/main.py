from collections import defaultdict
import operator as op

CMP = {'<': op.lt, '<=': op.le, '==': op.eq,
       '!=': op.ne, '>=': op.ge, '>': op.gt}

with open('data.txt', 'r') as f:
    instructions = [(lambda r, i, v, _, c_r, comp, c_v: [r, int(v) if i == 'inc' else -int(v), CMP[comp], c_r, int(c_v)])
                    (*row.split()) for row in f.readlines()]

registers = defaultdict(int)
highest_registered_value = 0
for (reg, v, comparer, cmp_reg, cmp_value) in instructions:
    registers[reg] += (v if comparer(registers[cmp_reg], cmp_value) else 0)
    highest_registered_value = max(registers[reg], highest_registered_value)


answer_part_1 = max(registers.values())
answer_part_2 = highest_registered_value

print(answer_part_1, answer_part_2)
