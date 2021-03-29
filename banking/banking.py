import random
import sqlite3
from typing import List, Any

conn = sqlite3.connect("card.s3db")

c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    pin TEXT, 
    balance INTEGER DEFAULT 0
    )""")
def communication():
    return int(input("1. Create an account\n2. Log into account \n0. Exit\n"))
def ask():
    ask = int(input("1. Balance\n"
                    "2. Add income \n"
                    "3. Do transfer\n"
                    "4. Close account\n"    
                    "5. Log out\n"    
                    "0. Exit\n"))
    return ask

class Account:

    def __init__(self):
        self.balance = 0
        self.pin = self.set_pin()
        self.card = self.set_card()

    @staticmethod
    def set_pin():
        pin = "".join([str(random.randint(0, 9)) for i in range(4)])
        return pin

    @staticmethod
    def luhn_algorithm(number):
        card_number = number
        multiple_n = [str(int(number) * 2) if i % 2 == 0 else str(number) for i, number in enumerate(number[:-1])]
        striped_n = [(int(number) - 9) if int(number) >= 10 else int(number) for number in multiple_n]
        check = sum(striped_n)
        final_number = str(10 - (check % 10))
        striped_n.append(final_number)
        number.join(final_number)
        if final_number == card_number[-1]:
            return False
        else:
            return True

    def create_card(self):
        sentence = True
        while sentence:
            main_number = str(400000) + "".join([str((random.randint(0, 9))) for i in range(10)])
            sentence = self.luhn_algorithm(main_number)
        return main_number

    def set_card(self):
        return self.create_card()

    def set_balance(self, number):
        self.balance = self.balance - number
        pass

    def menu(self, account_info):
        account_info_list = tuple(account_info)
        number_of_card = account_info_list[0][1]
        balance_of_card = account_info_list[0][-1]
        menu_ask = ask()
        while True:
            if menu_ask == 1:
                print(balance_of_card)
                menu_ask = ask()
            elif menu_ask == 2:
                income = int(input("Enter income:\n"))
                balance_of_card += income
                print("Income was added!\n")
                c.execute(f"UPDATE card SET balance = {balance_of_card} WHERE number = {number_of_card}")
                conn.commit()
                menu_ask = ask()
            elif menu_ask == 3:
                transfer_card = input("Transfer\nEnter card number:\n")
                check = self.luhn_algorithm(transfer_card)
                if check is False:
                    list_of_card_numbers = [card_number[0] for card_number in c.execute(
                        f"SELECT number FROM card").fetchall()]
                    if transfer_card not in list_of_card_numbers:
                        print("Such a card does not exist.")
                    elif transfer_card in list_of_card_numbers:
                        transfer_money = int(input("How much money you want to transfer:"))
                        if transfer_money > balance_of_card:
                            print("Not enough money!")
                        elif number_of_card == transfer_card:
                            print("You can't transfer money to the same account!")
                        elif transfer_money <= balance_of_card:
                            print("Success!")
                            balance_of_card -= transfer_money
                            c.execute(f"UPDATE card SET balance = {balance_of_card} WHERE number = {number_of_card}")
                            diff_account = list(c.execute(
                                f"SELECT balance FROM card WHERE number = {transfer_card}").fetchone())
                            conn.commit()
                            c.execute(f"UPDATE card SET balance = {transfer_money + diff_account[0]}"
                                      f" WHERE number = {transfer_card}")
                            conn.commit()
                elif check is True:
                    print("Probably you made a mistake in the card number. Please try again!")
                menu_ask = ask()
            elif menu_ask == 4:
                c.execute(f"DELETE FROM card WHERE number = {self.card}")
                conn.commit()
                print("The account has been closed!")
                menu_ask = ask()
            elif menu_ask == 5:
                return 2
            elif menu_ask == 0:
                print("Bye!")
                exit()

    def log(self, card_number, pin_number):
        list_n_p = [list(i) for i in c.execute(f"SELECT number,pin FROM card").fetchall()]
        if [card_number, pin_number] in list_n_p:
            print("You have successfully logged in!")
            account_info = c.execute(f"SELECT * FROM card WHERE number = {card_number}").fetchall()
            return self.menu(account_info)
        else:
            print("Wrong card number or PIN!")
            return 0

    def write(self):
        conn = sqlite3.connect("card.s3db")
        c = conn.cursor()
        c.execute(f"""INSERT INTO card (number,pin) VALUES({self.card},{self.pin})""")
        conn.commit()

def main():
    start = communication()
    while start != 0:
        if start == 1:
            new = Account()
            new.write()
            print("Your card has been created\nYour card number:")
            print(new.card)
            print("Your card PIN:")
            print(new.pin)
            start = communication()
        elif start == 2:
            news = new.log(input("Enter your card number:\n"), input("Enter your PIN:\n"))
            if news == 0:
                start = communication()
            elif news == 2:
                start = communication()

    else:
        conn.commit()
        print("Bye!")


if __name__ == "__main__":
    main()
