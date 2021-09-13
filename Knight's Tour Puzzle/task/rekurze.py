def rekurze(lst_of_lst, lst_of_positions):
    lenght_of_field = len(lst_of_positions)

    tuples = [(lst_of_positions[i % lenght_of_field],
               lst_of_positions[i+1 % lenght_of_field]) for i,_ in enumerate(lst_of_positions)]
    print(tuples)
    coords_change = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2))



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
    lst_of_positions = [int(i) for i in input("Start position:\n").split(" ")]
    rekurze(field, lst_of_positions)


if __name__ == "__main__":
    main()