def input_checking(lst_of_coord,n_rows,n_columns):
    try:
        assert len(lst_of_coord) == 2
        assert 0 < lst_of_coord[0] <= int(n_rows[0]) and 0 < lst_of_coord[1] <= int(n_columns)
    except (AssertionError, ValueError):
        print("Invalid dimension! check")
    else:
        lst_of_coord[0] -= 1
        lst_of_coord[1] = n_columns - lst_of_coord[1]
        return lst_of_coord


def dim_checking(lst_of_field):
    try:
        assert len(lst_of_field) == 2
        assert lst_of_field[0] > 0 and lst_of_field[1] > 0
    except (AssertionError, ValueError):
        print("Invalid dimension!")
    else:
        return lst_of_field


def printing(field, n_col):
    print(field)
    print(n_col)
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


def def_field(n_rows,n_columns):
    field_d = [[("_" * len(str(int(n_columns) * int(n_rows)))) for _ in range(int(n_rows))] for _ in
                   range(int(n_columns))]
    return field_d


def start_position(field, cords, n_rows, n_columns):
    change_field = field
    x, y = cords[0], cords[1]
    mark = " " * (len(str(n_rows * n_columns)) - 1) + "X"
    change_field[y][x] = mark
    return change_field


def for_possible_positions(field, coordinates):
    coordinates = tuple(coordinates)
    possible_coordinates = ((-2, +1), (-2, -1), (-1, +2), (-1, -2), (+2, +1), (+2, -1), (+1, +2), (+1, -2))
    x_main = coordinates[0]
    y_main = coordinates[1]

    new_coordinates = [(y_main + yi, x_main + xi) for xi, yi in possible_coordinates
                       if 0 <= y_main + yi < len(field) and
                       0 <= x_main + xi < len(field[0]) and (x_main + xi, y_main + yi) != (x_main,y_main)]
    #Potud je to ok.
    #Je možné vytvořit rekurzi
    for y,x in new_coordinates:
        try:
            total = [(y+yn,x+xn) for yn,xn in possible_coordinates if
                     0 <= y+yn <= len(field)-1 and
                     0 <= x+xn <= len(field[0])-1 and
                     (x+xn,y+yn) != (x_main,y_main)]
            field[y][x] = "{:>2}".format(len(total))
        except IndexError:
            pass
    return field


def main():
        try:
            n_rows, n_columns = dim_checking([int(i) for i in input("Enter your board dimensions: ").split(" ")])
            field_d = def_field(n_rows,n_columns)
        except TypeError:
            print("Invalid dimension! main1")
        else:
                try:
                    # input("Enter the knight's starting position: ").split(" ") swap back before check
                    positions = input_checking([int(i) for i in input("Enter the knight's starting position: ").split(" ")], n_rows,n_columns)
                    #Chyba vyse
                    start_field = start_position(field_d, positions, n_rows,n_columns)
                    print("B")
                    new_field = for_possible_positions(start_field, positions)
                    printing(new_field,n_rows,n_columns)
                except TypeError:
                    print("Invalid dimension! main 2")


if __name__ == "__main__":
    main()
