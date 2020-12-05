def get_id(s: str, r: list, c: list) -> int:
    if not s:
        return r[0] * 8 + c[0]
    return get_id(
        s[1:],
        r[len(r)//2 if s[0] == 'B' else 0:len(r)//2 if s[0] == 'F' else len(r)],
        c[len(c)//2 if s[0] == 'R' else 0:len(c)//2 if s[0] == 'L' else len(c)]
    )


ids = set((map(lambda x: get_id(x.strip(), list(range(128)), list(range(8))), open('input.txt', 'r').readlines())))
seat = (set(range(min(ids), last := max(ids))) - ids).pop()
print(f'Part 1: {last}')  # 926
print(f'Part 2: {seat}')  # 657
