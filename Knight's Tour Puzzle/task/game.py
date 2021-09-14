def input_checking(lst_of_coord, size_of_field):
    try:
        lst_of_coord = list(map(int, lst_of_coord))
        assert type(lst_of_coord) != list()
        assert len(lst_of_coord) == 2
        assert 0 < lst_of_coord[0] <= int(size_of_field[0]) and 0 < lst_of_coord[1] <= int(size_of_field[1])
    except (AssertionError, ValueError):
        print("Invalid dimension!")
    else:
        lst_of_coord[0] -= 1
        lst_of_coord[1] = size_of_field[1] - lst_of_coord[1]
        return tuple(lst_of_coord)


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

    return field_d


def start_position(field, cords, rows_columns):
    """Creation of field from input values."""
    change_field = field
    x, y = cords[0], cords[1]
    mark = " " * (len(str(rows_columns[0] * rows_columns[1])) - 1) + "X"
    change_field[y][x] = mark
    return change_field


def field_mark(field, position):
    """For changing the field in stage 5/6
    It changes the actual mark X with *."""
    length_of_mark = len(field[0][0])
    mark_symbol = "_" * length_of_mark + "X"
    for line in field:
        if mark_symbol in line:
            line[line.index(mark_symbol)] = length_of_mark * "*"
    x = position[1]
    y = position[0]
    field[y][x] = "_X"


def for_possible_positions(field, coordinates):
    coordinates = [tuple([coordinates[i], coordinates[i + 1]]) for i in range(0, len(coordinates), 2)]
    possible_coordinates = ((-2, +1), (-2, -1), (-1, +2), (-1, -2), (+2, +1), (+2, -1), (+1, +2), (+1, -2))
    x_main = coordinates[0][0]
    y_main = coordinates[0][1]
    new_coordinates = [(y_main + yi, x_main + xi) for xi, yi in possible_coordinates for y,x in coordinates
                       if 0 <= y_main + yi < len(field) and
                       0 <= x_main + xi < len(field[0]) and (x_main + xi, y_main + yi) != (x_main,y_main)]
    #Potud je to ok.
    #Je možné vytvořit rekurzi
    for y, x in new_coordinates:
        total = [(y+yn, x+xn) for yn,xn in possible_coordinates if
                     0 <= y+yn < len(field) and
                     0 <= x+xn < len(field[0]) and
                     (x+xn,y+yn) != (x_main, y_main)]
    new_coordinates = [(y_main + yi, x_main + xi) for xi, yi in possible_coordinates for y, x in coordinates
                       if 0 <= y_main + yi < len(field) and
                       0 <= x_main + xi < len(field[0]) and (x_main + xi, y_main + yi) != (x_main, y_main)]
    # Potud je to ok.
    # Je možné vytvořit rekurzi
    for y, x in new_coordinates:
        total = [(y + yn, x + xn) for yn, xn in possible_coordinates if
                 0 <= y + yn < len(field) and
                 0 <= x + xn < len(field[0]) and
                 (x + xn, y + yn) != (x_main, y_main)]
        field[y][x] = "{:>2}".format(len(total))
    return field


def main():
    n = 10
    while n != 0:
        try:
            dimensions = dim_checking(input("Enter your board dimensions: ").split(" "))
            field_d = def_field(dimensions)
        except TypeError:
            print("Invalid dimension!")
        else:
            while n != 0:
                try:
                    # input("Enter the knight's starting position: ").split(" ") swap back before check
                    positions = input_checking(tuple(input("Enter the knight's starting position: ").split(" ")), dimensions)
                    start_field = start_position(field_d, positions, dimensions)
                    new_field = for_possible_positions(start_field, positions)
                    printing(new_field,dimensions)

                except TypeError:
                    print("Invalid dimension!")
                    n -= 1
                else:
                    break
        break


if __name__ == "__main__":
    main()
