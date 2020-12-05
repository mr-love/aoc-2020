from functools import reduce

trees = list(map(lambda x: x.strip(), open('input.txt', 'r').readlines()))


def slope(dx, dy):
    hits = 0
    x = 0
    y = 0
    while y < len(trees):
        line = trees[y]
        y += dy
        if line[x] == '#':
            hits += 1
        x += dx
        if x >= len(line):
            x -= len(line)
    return hits


collisions = [
    slope(1, 1),
    slope(3, 1),
    slope(5, 1),
    slope(7, 1),
    slope(1, 2)
]
product = reduce(lambda i, j: i * j, collisions)
print(
    f'Part 1: {collisions[1]}\n'
    f'Part 2: {product}'
)
