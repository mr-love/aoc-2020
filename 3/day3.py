from math import prod

trees = list(map(lambda x: x.strip(), open('input.txt', 'r').readlines()))


def path(d):
    hits, x, y = 0, 0, 0
    while y < len(trees):
        line = trees[y]
        hits += 1 if line[x] == '#' else 0
        x, y = x+d[0], y+d[1]
        x -= len(line) if x >= len(line) else 0
    return hits


print(f'Part 1: {path((3, 1))}')  # 299
print(f'Part 2: {prod(map(path, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))}')  # 3621285278
