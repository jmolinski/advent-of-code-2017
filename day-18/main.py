from collections import deque


class Executor:
    def __init__(self, registers, instructions, part_1=False, e_id=0):
        self.instructions = instructions
        self.registers = registers.copy()
        self.pos = 0
        self.last_received = 0
        self.last_sent = 0
        self.sent_values = 0
        self.in_buffer = deque()
        self.e_id = e_id

        self.operations = {
            'set': lambda x, y: self.registers.update({x: self.get_val(y)}),
            'add': lambda x, y: self.registers.update({x: self.get_val(x) + self.get_val(y)}),
            'mul': lambda x, y: self.registers.update({x: self.get_val(x) * self.get_val(y)}),
            'mod': lambda x, y: self.registers.update({x: self.get_val(x) % self.get_val(y)}),
            'jgz': lambda x, y: setattr(self, 'pos',
                                        self.pos + self.get_val(y) - 1 if self.get_val(x) > 0 else self.pos)
        }

        if part_1:
            self.operations.update({
                'snd': lambda x: setattr(self, 'last_sent', self.get_val(x)),
                'rcv': lambda x: setattr(self, 'last_received',
                                         self.last_sent if self.get_val(x) else self.last_received),
            })
        else:
            def send(x):
                self.partner.in_buffer.appendleft(self.get_val(x))
                self.sent_values += 1

            def receive(x):
                if not len(self.in_buffer):
                    self.pos -= 1
                else:
                    self.registers[x] = self.in_buffer.pop()

            self.operations.update({
                'snd': send,
                'rcv': receive,
            })

    def get_val(self, v):
        if len(v) == 1 and v.isalpha():
            return self.registers.get(v, 0)
        return int(v)

    def set_partner(self, p_executor):
        self.partner = p_executor

    def exec_till_first_received(self):
        while not self.last_received:
            self.run_next_operation()

        return self.last_received

    def run_next_operation(self):
        op, *args = self.instructions[self.pos]
        self.operations[op](*args)
        self.pos += 1

    def locked(self):
        return self.instructions[self.pos][0] == 'rcv' and len(self.in_buffer) == 0

    def run_until_lock(self):
        while not self.locked():
            self.run_next_operation()


INSTRUCTIONS = [l.split() for l in open('data.txt', 'r').readlines()]

p1_executor = Executor({}, INSTRUCTIONS, part_1=True)
p1_executor.exec_till_first_received()

p2_executor_0 = Executor({'p': 0}, INSTRUCTIONS, e_id=0)
p2_executor_1 = Executor({'p': 1}, INSTRUCTIONS, e_id=1)
p2_executor_0.set_partner(p2_executor_1)
p2_executor_1.set_partner(p2_executor_0)

while not p2_executor_0.locked() or not p2_executor_1.locked():
    p2_executor_0.run_until_lock()
    p2_executor_1.run_until_lock()

answer_part_1 = p1_executor.last_received
answer_part_2 = p2_executor_1.sent_values

print(answer_part_1, answer_part_2)
