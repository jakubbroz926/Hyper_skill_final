def help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n"
              "Special commands: !help !done")
    
    
def entry():
    global ent
    ent = input("Choose formatter: ")
    
    
def main():
    entry()
    viable_commands = ["plain", "bold","italic","header","link","inline-code","ordered-list","unordered-list","new-line"]
    while True:
        if ent in viable_commands:
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
