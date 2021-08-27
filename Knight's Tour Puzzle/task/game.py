def input_checking(lst_of_coord):
    try:
        lst_of_coord = list(map(int, lst_of_coord))
        assert type(lst_of_coord) != list()
        assert len(lst_of_coord) == 2
        assert 0 < lst_of_coord[0] < 9 and 0 < lst_of_coord[1] < 9
    except (AssertionError,ValueError):
        print("Invalid dimension!")
    else:
        return lst_of_coord


def field(cords):
    #ukládání pole do dalších kroků
    try:
        x = cords[0]
        y = cords[1]
        line = "-"*20
        print(line)
        for j in range(8,0,-1):
            print(f"{j}| ", end="")
            for i in range(8):
                if i == x-1 and j == y:
                    print("X ", end = "")
                else:
                    print("_ ", end="")
            print("|", end="\n")
        print(line,end="\n   ")
        for i in range(8):
            print(i+1,end=" ")
    except TypeError:
        pass
def main():
    numbers = input("Enter the knight's starting position: ").split(" ")
    cords = input_checking(numbers)
    field(cords)

if __name__ == "__main__":
    main()