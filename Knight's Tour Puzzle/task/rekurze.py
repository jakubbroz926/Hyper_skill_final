def rekurze(lst_of_lst,lst_of_positions):
    y_x = [((len(lst_of_lst) - lst_of_positions[i+1 % len(lst_of_positions)])-1,
            (lst_of_positions[i % len(lst_of_positions)]))
            for i in range(0, len(lst_of_positions), 2)]
    possible_coordinates = ((-2, +1), (-2, -1), (-1, +2), (-1, -2), (+2, +1), (+2, -1), (+1, +2), (+1, -2))
    print(y_x)
    lst_of_lst[y_x[0][0]][y_x[0][1]] = "X"
    print(lst_of_lst)


def def_field(sizes):
    field_d = [[("_" * len(str(int(sizes[1]) * int(sizes[0])))) for _ in range(int(sizes[0]))] for _ in
               range(int(sizes[1]))]
    for line in field_d:
        print(line)
    return field_d


def main():
    sizes_of_field = [int(i) for i in input("Size of x and y:\n").split(" ")]
    print(sizes_of_field)
    field = def_field(sizes_of_field)
    lst_of_positions = [int(i)-1 for i in input("Start position:\n").split(" ")]
    rekurze(field, lst_of_positions)


if __name__ == "__main__":
    main()