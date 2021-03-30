import math
import argparse


class Loan:

    def __init__(self):
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
        n = math.log(payment/(payment - i * principal), 1+i)
        n_y, n_m = (math.ceil(n)//12), (math.ceil(n) - 12 * (math.ceil(n)//12))
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

def testing(test):
    print(test)

def main():
    loan_parser = argparse.ArgumentParser("Informations for counting loan")
    loan_parser.add_argument("--type",type = str)
    loan_parser.add_argument("--principal",type = int)
    loan_parser.add_argument("--period",type = int)
    loan_parser.add_argument("--intetest",type = float)
    args = loan_parser.parse_args()
    print(type(args))

    new_loan = Loan()


if __name__ == "__main__":
    main()