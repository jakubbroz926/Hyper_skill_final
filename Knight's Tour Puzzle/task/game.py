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


def start_position(field, cords, rows_columns):
    change_field = field
    x, y = cords[0], cords[1]
    mark = " " * (len(str(rows_columns[0] * rows_columns[1])) - 1) + "X"
    change_field[len(field) - y][x - 1] = mark
    return change_field


def for_possible_positions(field, coordinates):
    possible_coordinates = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2))
    x, y = coordinates[0] - 1, len(field[0]) - coordinates[1]
    for (xim, yim) in possible_coordinates:
        try:
            if (len(field[0])-1 >= x+xim >= 0) and (len(field[1])-1 >= y+yim >= 0):
                total = 0
                for (xis, yis) in possible_coordinates:
                    if (len(field[0])-1 >= xim+xis >= 0) and (len(field[1])-1 >= yim+yis >= 0):
                        print(len(field[0])-1 >= xim+xis >= 0) and (len(field[1])-1 >= yim+yis >= 0)
                        print(xim+xis,yim+yis,total,"\n")
                        total = + 1

                        field[y + yim][x + xim] = "{:>}".format(total)
                print("S",field,total)
        except IndexError:
            pass
    return field


def possible_positions(field, coordinates, n = 2):
    possible_coordinates = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2))
    total = 0
    if n == 1:
        return field
    else:
        x, y = coordinates[0] - 1, len(field[0]) - coordinates[1]
        for _, (xi, yi) in enumerate(possible_coordinates):
            try:
                if (y + yi >= 0) and (x + xi >= 0):
                    total += 1
                    field[y + yi][x + xi] = "{:>2}".format(
                        total)  # na konci dané recurse se vrátí číslo označíjí počet možných skoků
                    print(field)
                    return possible_positions(field, [x + xi, y + yi], n - 1)
            except IndexError:
                pass


def main():
    while True:
        try:
            #dim_checking(input("Enter your board dimensions: ").split(" ")) swap back before check
            dim = [4,4]
            dimensions = dim
            field_d, rows_columns = def_field(dimensions)
        except TypeError:
            print("Invalid dimension!")
        else:
            while True:
                try:
                    #input("Enter the knight's starting position: ").split(" ") swap back before check
                    positions = input_checking([2,2], dimensions)
                    start_field = start_position(field_d, positions, rows_columns)
                    for_possible_positions(start_field, positions)
                    # printing(new_field, rows_columns)
                except TypeError:
                    print("Invalid dimension!")
                else:
                    break
        break


if __name__ == "__main__":
    main()
