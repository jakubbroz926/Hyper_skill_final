def input_checking(lst_of_coord, n_rows, n_columns):
    length_of_lst = len(lst_of_coord)
    try:
        assert len(lst_of_coord) == 2
        assert 0 < lst_of_coord[0] <= int(n_rows) and 0 < lst_of_coord[1] <= int(n_columns)
    except (AssertionError, ValueError):
        print("Invalid dimension! input")
    else:
        lst_of_coord[0] -= 1
        lst_of_coord[1] = n_columns - lst_of_coord[1]
        y_x_list_of_tuples = [(lst_of_coord[i + 1 % length_of_lst],lst_of_coord[i % length_of_lst])
                for i in range(0, length_of_lst, 2)]
        return y_x_list_of_tuples


def dim_checking(lst_of_field):
    try:
        assert len(lst_of_field) == 2
        assert lst_of_field[0] > 0 and lst_of_field[1] > 0
    except (AssertionError, ValueError):
        print("Invalid dimension! dimension")
    else:
        return lst_of_field


def field_marking(field,cell_size, positions):
    old_marker = " " * (cell_size - 1) + "X"
    unpacked_positions = enter_to_tuple(positions)
    for position in unpacked_positions:
        y, x = position[0],position[1]
        field[y][x] = old_marker
    print(field)
    return field
    #Change old mark X for used mark *
    for line in field:
        if old_marker in line:
            line[old_marker] = " " * (cell_size-1)+"*"



    # field[y][x] = "{:>2}".format(len(total))



def printing(field,cell_size, n_rows, n_columns):
    size_of_field = n_columns
    line = " " + "-" * (3 + n_rows * (cell_size + 1))
    print(line)
    for field_line, i in zip(field, range(size_of_field, 0, -1)):
        print(f"{i}| ", end = "")
        print(" ".join(field_line), end = "")
        print(" |", end = "\n")
    print(line, end = "\n" + " " * (cell_size + 2))
    for i in range(n_rows):
        print(f"{i + 1}" + " " * cell_size, end = "")
    print("\n")


def enter_to_tuple(lst, result = list()):
    for i in lst:
        if not isinstance(i, tuple):
            return enter_to_tuple(i)
        else:
            result.append(i)
    return result


def def_field(n_rows, n_columns):
    field_d = [[("_" * len(str(int(n_columns) * int(n_rows)))) for _ in range(int(n_rows))] for _ in
               range(int(n_columns))]
    return field_d


def start_position(field,cell_size, cords):
    change_field = field
    y,x = cords[0][0],cords[0][1]
    mark = " " * (cell_size - 1) + "X"
    change_field[y][x] = mark
    return change_field


def first_coordinate(n_rows, n_columns, coordinates):
    possible_coordinates = ((-2, +1), (-2, -1), (-1, +2), (-1, -2), (+2, +1), (+2, -1), (+1, +2), (+1, -2))
    first_coordinates = [[(y_main + yi, x_main + xi) for xi, yi in possible_coordinates
                          if 0 <= y_main + yi < n_columns and
                          0 <= x_main + xi < n_rows if (x_main + xi, y_main + yi) != (x_main, y_main)]
                         for (y_main, x_main) in coordinates]
    return first_coordinates


def main():
    try:
        n_rows, n_columns = dim_checking([int(i) for i in input("Enter your board dimensions: ").split(" ")])
        field_d = def_field(n_rows, n_columns)
        cell_size = int(len(str(n_rows * n_columns)))
    except TypeError:
        print("Invalid dimension! main1")
    else:
        try:
            y_x_tuples = input_checking([int(i) for i in input("Enter the knight's starting position: ").split(" ")],
                                       n_rows, n_columns)
            start_field = start_position(field_d,cell_size, y_x_tuples)
            first_position = first_coordinate(n_rows, n_columns, y_x_tuples)
            new_field = field_marking(start_field,cell_size,first_position,)
            printing(new_field,cell_size, n_rows, n_columns)
        except (TypeError, ValueError):
            print("Invalid dimension! main 2")
        else:
            pass
            #There will be lines for asking newer lines


if __name__ == "__main__":
    main()
