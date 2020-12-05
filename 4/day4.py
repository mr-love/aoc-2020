validators = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: (150 <= int(x[:-2]) <= 193 and 'cm' in x) or (59 <= int(x[:-2]) <= 76 and 'in' in x),
    'hcl': lambda x: x.startswith('#') and len(x) == 7 and int(x[1:], 16),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: int(x) and len(x) == 9,
    'cid': lambda x: True
}


def validator(part):
    field, value = part.split(':')
    try:
        return validators[field](value)
    except:
        return


def validate(passport: str) -> (bool, bool):
    parts = passport.split(' ')
    hasfields = all([k in [p.split(':')[0] for p in parts] for k in validators.keys() if k != 'cid'])
    return (
        hasfields,
        hasfields and all([validator(p) for p in parts])
    )


passports_file = open('input.txt', 'r')
passports = [p.replace('\n', ' ').strip() for p in passports_file.read().split('\n\n')]
valid = 0
has_fields = 0
for passport in passports:
    f, v = validate(passport)
    has_fields += f
    valid += v
print(f'Part 1: {has_fields}')
print(f'Part 2: {valid}')
