lines = open('input.txt', 'r').readlines()

biggest_id = 0
ids = [r * 8 + c for r in range(1, 127) for c in range(8)]
for line in lines:
    rows = list(range(128))
    cols = list(range(8))
    for s in line:
        if s == 'F':
            rows = rows[:len(rows)//2]
        elif s == 'B':
            rows = rows[len(rows)//2:]
        elif s == 'L':
            cols = cols[:len(cols)//2]
        elif s == 'R':
            cols = cols[len(cols)//2:]
    id = rows[0] * 8 + cols[0]
    ids.remove(id)
    biggest_id = max(id, biggest_id)

print(f'Part 1: {id}')
print(f'Part 2: {[id for i, id in enumerate(ids) if ids[i-1] != id-1][1]}')
