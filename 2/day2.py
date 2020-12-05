def process_record(record: str) -> tuple:
    occurrences, character, password = record.replace(':', '').split(' ')
    lower, upper = map(int, occurrences.split('-'))
    return lower, upper, character, password


def validator_1(record: tuple) -> bool:
    o, u, c, p = record
    return o <= p.count(c) <= u


def validator_2(record: tuple) -> bool:
    o, u, c, p = record
    return (p[o-1] == c) != (p[u-1] == c)


db = map(process_record, open('input.txt', 'r').readlines())
valid_1: int = 0
valid_2: int = 0
for line in db:
    valid_1 += validator_1(line)
    valid_2 += validator_2(line)

print(
    f'Part 1: {valid_1}\n'
    f'Part 2: {valid_2}'
)
