def input_checking(lst_of_coord, size_of_field):
    try:
        lst_of_coord = list(map(int, lst_of_coord))
        assert type(lst_of_coord) != list()
        assert len(lst_of_coord) == 2
        assert 0 < lst_of_coord[0] <= int(size_of_field[0]) and 0 < lst_of_coord[1] <= int(size_of_field[1])
    except (AssertionError, ValueError):
        print("Invalid dimension!")
    else:
        return lst_of_coord


def dim_checking(lst_of_field):
    try:
        field_coord = list(map(int, lst_of_field))
        assert len(field_coord) == 2
        assert field_coord[0] > 0 and field_coord[1] > 0
    except (AssertionError, ValueError):
        print("Invalid dimension!")
    else:
        return field_coord


def printing(field, n_col):
    size_of_field = n_col[1]
    cell_size = int(len(str(n_col[0] * n_col[1])))

    line = " " + "-" * (3 + n_col[0] * (cell_size + 1))
    print(line)
    for field_line, i in zip(field, range(size_of_field, 0, -1)):
        print(f"{i}| ", end = "")
        print(" ".join(field_line), end = "")
        print(" |", end = "\n")
    print(line, end = "\n" + " " * (cell_size + 2))
    for i in range(n_col[0]):
        print(f"{i + 1}" + " " * cell_size, end = "")
    print("\n")


def def_field(sizes):
    field_d = [[("_" * len(str(int(sizes[1]) * int(sizes[0])))) for _ in range(int(sizes[0]))] for _ in
               range(int(sizes[1]))]
    return field_d, sizes


def field_change(field, cords, n_col):
    change_field = field
    x, y = cords[0], cords[1]
    mark = " " * (len(str(n_col[0] * n_col[1])) - 1) + "X"
    change_field[len(field) - y][x - 1] = mark
    return change_field, n_col


def possible_positions(field, coordinates):

    x, y = coordinates[0]-1, len(field[0]) - coordinates[1]
    coords_change = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2))
    for i, (xi, yi) in enumerate(coords_change):
        try:
            if (y+yi >= 0) and (x+xi >= 0):
                field[0][y+yi][x+xi] = "{:>2}".format(0)
        except IndexError:
            pass
    return field[0]



def main():
    while True:
        try:
            dimensions = dim_checking(input("Enter your board dimensions: ").split(" "))
            field_d, n_col = def_field(dimensions)
        except TypeError:
            print("Invalid dimension!")
        else:
            while True:
                try:
                    numbers = input_checking(input("Enter the knight's starting position: ").split(" "), dimensions)
                    new_field = possible_positions(field_change(field_d, numbers, n_col), numbers)
                    printing(new_field, n_col)
                except TypeError:
                    print("Invalid dimension!")
                else:
                    break
        break

if __name__ == "__main__":
    main()
