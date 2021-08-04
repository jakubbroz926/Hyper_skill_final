def help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n"
          "Special commands: !help !done")


def entry():
    global ent
    ent = input("Choose formatter: ")


def get_text():
    return input("Text: ")


def plain():
    return get_text()


def bold():
    return "**" + get_text() + "**"


def italic():
    return "*" + get_text() + "*"



def header():
    while True:
        level = int(input("Level:"))
        if 1 <= level <= 6:
            text = input("Text:")
            return f"{level * '#'} {text}\n"
            break
        else:
            print("The level should be within the range of 1 to 6")
            continue


def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"

def inline_code():
    return "`" + get_text() + "`"


def main():
    line_of_text = ""
    entry()
    viable_commands = ["plain", "bold", "italic", "header", "link"]
    while True:
        if ent in viable_commands:
            line_of_text += eval(ent + "()")
            print(line_of_text)
            entry()
        elif ent ==  "inline-code":
            line_of_text += inline_code()
            print(line_of_text)
            entry()
        elif ent == "new-line":
            print(line_of_text)
            print()
            entry()
        elif ent == "!done":
            quit()
        elif ent == "!help":
            help()
            entry()
        else:
            print("Unknown formatting type or command")
            entry()


if __name__ == "__main__":
    main()