import random
def luhn_algorithm():
    main_number = str(400000) + "".join([str((random.randint(0, 9))) for i in range(10)])
    multn = [str(int(number) * 2) if i % 2 == 0 else str(number) for i, number in enumerate(main_number[:-1])]
    striped_n = [(int(number) - 9) if int(number) >= 10 else int(number) for number in multn]
    check = sum(striped_n)
    finald = str(10 - (check % 10))
    striped_n.append(finald)
    main_number.join(finald)
    return print(main_number)

def create_card():
    main_number = str(400000) + "".join([str((random.randint(0, 9))) for i in range(9)])
    print(main_number)
    total = sum([int(i) for i in main_number])
    finald = str(10 - (total % 10))
    if finald != str(10):
        main_number += finald
    else:
        main_number += str(0)
    return main_number
