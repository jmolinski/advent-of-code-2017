class Executor:
    def __init__(self, registers, instructions):
        self.instructions = instructions
        self.registers = registers.copy()
        self.pos = 0
        self.times_mul_invoked = 0

        def jump_if_nonzero(x, y):
            if self.get_val(x) != 0:
                self.pos = self.pos + self.get_val(y) - 1

        def multiplique(x, y):
            self.registers[x] = self.get_val(x) * self.get_val(y)
            self.times_mul_invoked += 1

        self.operations = {
            'set': lambda x, y: self.registers.update({x: self.get_val(y)}),
            'sub': lambda x, y: self.registers.update({x: self.get_val(x) - self.get_val(y)}),
            'mul': multiplique,
            'jnz': jump_if_nonzero,
        }

    def get_val(self, v):
        if len(v) == 1 and v.isalpha():
            return self.registers.get(v, 0)
        return int(v)

    def run_next_operation(self):
        op, *args = self.instructions[self.pos]
        if self.pos == 20:
            print(self.pos, op, self.registers)
        self.operations[op](*args)
        self.pos += 1

    def run_until_end(self):
        while 0 <= self.pos < len(self.instructions):
            self.run_next_operation()


def isprime(n):
    if n == 2:
        return True

    elif n < 2 or not n & 1:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


INSTRUCTIONS = [l.split() for l in open('data.txt', 'r').readlines()]

p1_executor = Executor({}, INSTRUCTIONS)
p1_executor.run_until_end()

answer_part_1 = p1_executor.times_mul_invoked
answer_part_2 = sum(not isprime(b) for b in range(105700, 122701, 17))

print(answer_part_1, answer_part_2)
