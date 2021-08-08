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
def n_rows():
    n_rows = int(input("Number of rows: "))
    while n_rows <= 0:
        print("The number of rows should be greater than zero")
        n_rows = int(input("Number of rows: "))
    return n_rows
def dered():  #i didnt want change function list() so I picked string which is contained in both list formatters
    lines = [input(f"{i}.Row ")for i in range(1,n_rows()+1)]
    ordered_line = ""
    for i,line in enumerate(lines):
        if "un" in ent:
            ordered_line += f"* {line}\n"
        else:
            ordered_line += f"{i+1}. {line}\n"
    return ordered_line
    
def done(text):
    file = open("output.md","w+")
    file.write(text)
    file.close()
    quit()
    
def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"

def inline_code():
    return "`" + get_text() + "`"


def main():
    line_of_text = ""
    entry()
    viable_commands = ["plain", "bold", "italic", "header", "link","ordered-list","unordered-list"]
    while True:
        if ent in viable_commands:
            if len(ent) > 6:
                line_of_text += dered()
                print(line_of_text)
                entry()
            else:
                line_of_text += eval(ent + "()")
                print(line_of_text)
                entry()
        elif ent ==  "inline-code":
            line_of_text += inline_code()
            print(line_of_text)
            entry()
        elif ent == "new-line":
            line_of_text += "\n"
            print(line_of_text)
            entry()
        elif ent == "!done":
            done(line_of_text)
        elif ent == "!help":
            help()
            entry()
        else:
            print("Unknown formatting type or command")
            entry()


if __name__ == "__main__":
    main()