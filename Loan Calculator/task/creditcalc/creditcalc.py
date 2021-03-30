import math
import argparse


class Loan:

    def __init__(self, args):
        for key in args:
            setattr(self, key, args[key])
        self.counting_type()

    def counting_type(self):
        if self.__getattribute__("type") == "diff":
            self.diff()
        else:
            self.annuity()

    def diff(self):
        P = self.__getattribute__("principal")
        n = self.__getattribute__("periods")
        i = self.__getattribute__("interest")/(12*100)
        total = 0
        for m in range(1, n+1):
            dm = math.ceil(P/n + i*(P - (P * (m-1)/n)))
            total += dm
            print(f"Month {m}: payment is {dm}")
        print(f"Overpayment = {total-P}")

    def annuity(self):
        i = self.__getattribute__("interest") / (12 * 100)
        if "periods" not in self.__dict__:
            P = self.__getattribute__("principal")
            p = self.__getattribute__("payment")
            n = math.ceil(math.log(p / (p - i * P), 1 + i))
            print(f"It will take {n // 12} years to repay this loan!")
            print(f"Overpayment = {n // 12 * p-P} ")
        elif "payment" not in self.__dict__:
            P = self.__getattribute__("principal")
            n = self.__getattribute__("periods")
            p = math.ceil(P * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
            print(f"Your annuity payment = {p}!")
            print(f"Your overpayment = {n*p - P} ")
        else:
            p = self.__getattribute__("payment")
            n = self.__getattribute__("periods")
            principal = math.ceil(p / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {math.ceil(n * p - principal)}")


def check_args(args):
    remove = [k for k, v in args.items() if v is None]
    for key in remove:
        del args[key]
    if (len(args) < 4)\
        or (args["type"] != "diff" and args["type"] != "annuity")\
        or ("payment" in args.keys() and "diff" == args["type"])\
        or ("interest" not in args.keys()) \
        or (any([v < 0 for k, v in args.items() if isinstance(v, float) or isinstance(v, int)])):
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
