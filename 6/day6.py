from functools import reduce

p1, p2 = list(), list()
lines = open('input.txt', 'r')
for group in lines.read().split('\n\n'):
    a = [set(answers) for answers in group.strip().split('\n')]
    p1.append(len(reduce(lambda x, y: x | y, a)))
    p2.append(len(reduce(lambda x, y: x & y, a)))

print(f'Part 1: {sum(p1)}')  # 6291
print(f'Part 2: {sum(p2)}')  # 3052
