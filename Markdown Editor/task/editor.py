def done(input):
    if input == "!done":
        return quit()
def help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n"
              "Special commands: !help !done")

def main():
    viable_commands = ["plain", "bold","italic","header","link","inline-code","ordered-list","unordered-list","new-line"]
    entry = input("Choose formatter: ")
    while True:
        if entry in viable_commands:
            entry = input("Choose formatter: ")
        elif entry == "!done":
            quit()
        elif entry == "!help":
            help()
            entry = input("Choose formatter: ")
        else:
            print("Unknown formatting type or command")
            entry = input("Choose formatter: ")

if __name__ == "__main__":
    main()