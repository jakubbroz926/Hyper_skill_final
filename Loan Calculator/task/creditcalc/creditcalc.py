import math
import argparse


class Loan:

    def __init__(self, args):
        for key in args:
            setattr(self, key, args[key])
        self.choice()

    def choice(self):
        if self.__getattribute__("type") == "diff":
            self.diff()
        else:
            self.annuity()

    def diff(self):#first write diff method
        print(self.__getattribute__("principal"))

    def annuity(self):
        print(self.__getattribute__("payment"))


def check_args(args):
    remove = [k for k, v in args.items() if v is None]
    for key in remove:
        del args[key]
    if len(args) < 4:
        print("A")
        print("Incorrect parameters.")
        return quit()
    elif args["type"] != "diff" and args["type"] != "annuity":
        print("B")
        print("Incorrect parameters.")
        return quit()
    elif "payment" in args.keys() and "diff" == args["type"]:
        print("C")
        print("Incorrect parameters.")
        return quit()
    elif "interest" not in args.keys():
        print("D")
        print("Incorrect parameters.")
        return quit()
    elif any([v < 0 for k, v in args.items() if isinstance(v, float) or isinstance(v, int)]):
        print("E")
        print("Incorrect parameters.")
        return quit()
    else:
        return args


def main():
    loan_parser = argparse.ArgumentParser("Information for counting loan")
    loan_parser.add_argument("--type", type = str)
    loan_parser.add_argument("--principal", type = int)
    loan_parser.add_argument("--periods", type = int)
    loan_parser.add_argument("--interest", type = float)
    loan_parser.add_argument("--payment", type = int)
    args = vars(loan_parser.parse_args())
    new_loan = Loan(check_args(args))


if __name__ == "__main__":
    main()
