from collections import defaultdict
import re


class TuringMachine:
    tape = defaultdict(int)
    cursor = 0
    state = ''
    states = {}
    steps = 0

    def __init__(self, starting_state, states):
        self.state = starting_state
        self.states = states

    def goto_state(self, s):
        self.state = s

    def write_value(self, v):
        self.tape[self.cursor] = int(v)

    def move_slot(self, to_the):
        self.cursor += 1 if to_the == 'right' else -1

    def run_step(self):
        for op_name, args in self.states[self.state][self.tape[self.cursor]]:
            getattr(self, op_name)(*args)

        self.steps += 1

    def run_steps(self, n=1):
        for _ in range(n):
            self.run_step()

    def get_diagnostic_checksum(self):
        return list(self.tape.values()).count(1)


class Parser:
    INSTR_MAPPING = {
        'write the value': 'write_value',
        'move one slot to the': 'move_slot',
        'continue with state': 'goto_state',
    }

    @classmethod
    def parse_instruction(cls, instr):
        instr = instr.strip().replace('- ', '')
        *op_name, args = instr.split(' ')

        op = cls.INSTR_MAPPING[' '.join(op_name).lower()]

        return (op, (args, ))

    @classmethod
    def parse_state(cls, instructions):
        reg = r'value is ([01]):(.+?)\.(.+?)\.(.+?)\.'

        return {int(i): [cls.parse_instruction(op) for op in ops]
                for i, *ops in re.findall(reg, instructions, re.S)}

    def parse_blueprints(self, data):
        self.init_state = re.search(r'in state (\w)?', data).groups(1)[0]
        self.exec_until = int(
            re.search(r'after (\d+) steps', data).groups(1)[0])

        self.states = {s: self.parse_state(instructions)
                       for s, instructions
                       in re.findall(r'In state (\w):(.+?)\n\n', data, re.S)}

    def __init__(self, data):
        self.parse_blueprints(data)


with open('data.txt') as f:
    parsed = Parser(f.read() + '\n\n')

turing_machine = TuringMachine(parsed.init_state, parsed.states)
turing_machine.run_steps(parsed.exec_until)

answer = turing_machine.get_diagnostic_checksum()

print(answer)
