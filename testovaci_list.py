def print_number(number):
    number = str(number)
    if len(number) == 0:
        return 0
    else:
        return int(number[0])+print_number(number[1:])
number = 10151561
print(print_number(number))