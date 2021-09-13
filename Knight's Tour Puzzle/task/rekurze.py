def rekurze(lst_of_lst, lst_of_positions):
    cordination_changes = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2))
    length_of_field = len(lst_of_lst)
    length_of_pos = len(lst_of_positions)
    tuples = [(lst_of_positions[i % length_of_pos] - 1,
               length_of_field - lst_of_positions[i + 1 % length_of_pos]) for i in range(0, length_of_pos, 2)]
#Toto se provede vzdy
    new_positions = [[(y+yi,x+xi) for yi,xi in cordination_changes] for x,y in tuples] #zde je prohozeni x a y v listu
    print(new_positions)




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