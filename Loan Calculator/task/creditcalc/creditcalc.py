import math
import argparse


class Loan:

    def __init__(self, args):
        self.type_of_counting = input("What do you want to calculate?\n"
                                      "type 'n' for number of monthly payments\n"
                                      "type 'a' for the monthly payment:\n"
                                      "type 'p' for loan principal:\n")
        if self.type_of_counting.lower() == "n":
            print(self.months())
        elif self.type_of_counting.lower() == "a":
            print(self.annuity())
        elif self.type_of_counting.lower() == "p":
            print(self.principal_loan())

    @staticmethod
    def months():
        principal = int(input("Enter your principal loan:"))
        payment = int(input("Enter your monthly payment:"))
        interest = float(input("Enter the loan interest:"))
        i = interest / (12 * 100)
        n = math.log(payment / (payment - i * principal), 1 + i)
        n_y, n_m = (math.ceil(n) // 12), (math.ceil(n) - 12 * (math.ceil(n) // 12))
        if n_y == 0:
            return f"It will take {n_m} months to repay this loan!"
        elif n_m == 0:
            return f"It will take {n_y} years to repay this loan!"
        else:
            return f"It will take {n_y} years and {n_m} months to repay this loan!"

    @staticmethod
    def annuity():
        principal = int(input("Enter your principal loan:"))
        months = int(input("Enter the number of periods:"))
        interest = float(input("Enter the loan interest:"))
        i = interest / (12 * 100)
        an = math.ceil(principal * ((i * (1 + i) ** months) / ((1 + i) ** months - 1)))
        return f"Your monthly payment = {an}!"

    @staticmethod
    def principal_loan():
        payment = float(input("Enter the annuity payment:"))
        months = int(input("Enter the number of periods:"))
        interest = float(input("Enter the loan interest:"))
        i = interest / (12 * 100)
        principal = round(payment / ((i * (1 + i) ** months) / ((1 + i) ** months - 1)))
        return f"Your loan principal = {principal}!"


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
