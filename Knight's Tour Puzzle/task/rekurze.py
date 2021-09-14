def first_position(lst_of_lst, lst_of_positions):
    length_of_field = len(lst_of_lst)
    length_of_pos = len(lst_of_positions)
    tuples = list()
    for i in range(0, length_of_pos, 2):
        tuples.append((lst_of_positions[i % length_of_pos] - 1,
                       length_of_field - lst_of_positions[i + 1 % length_of_pos]))
    coordination_changes = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2))
    new_positions = [[(y + yi, x + xi) for yi, xi in coordination_changes if 0 <= y + yi < length_of_field and
                      0 <= x + xi < len(lst_of_lst[0])
                      and (x + xi, y + yi) != (x, y)
                      ] for x, y in tuples]  # zde je prohozeni x a y v listu
    return new_positions


def rekurze(field, positions):
    coordination_changes = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2))
    length = len(field)
    for line in positions:
        if len(line) == 0:
            print(line)
        else:
            rekurze(field, [[(y + yi, x + xi) for yi, xi in coordination_changes if 0 <= y + yi < length and
                      0 <= x + xi < length
                      and (x + xi, y + yi) != (x, y)
                      ] for x, y in line])


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
    positions = first_position(field, lst_of_positions)
    rekurze(field,positions)

if __name__ == "__main__":
    main()
