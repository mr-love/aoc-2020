expenses = []
expenses_p2 = set()
target_sum = 2020
expense_report = map(int, open('input.txt', 'r').readlines())
for next_expense in expense_report:
    # part 2
    for e in expenses_p2:
        ps, e1, e2 = e
        s = ps + next_expense
        if s == target_sum:
            p = e1 * e2 * next_expense
            print(
                f'Part 2: {p}\n'
                f'\t{e1} + {e2} + {next_expense} = 2020\n'
                f'\t{e1} * {e2} * {next_expense} = {p}'
            )
    # part 1
    for expense in expenses:
        s = expense + next_expense
        if s == target_sum:
            p = expense * next_expense
            print(
                f'Part 1: {p}\n'
                f'\t{expense} + {next_expense} = 2020\n'
                f'\t{expense} * {next_expense} = {p}'
            )
        elif s < target_sum:
            expenses_p2.add((s, expense, next_expense))
    expenses.append(next_expense)
