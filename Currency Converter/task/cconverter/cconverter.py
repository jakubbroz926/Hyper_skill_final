n_conicoins = float(input())
rates = open("rates.txt", "w+", encoding = "utf-8")
currencies = ["RUB : 2.98 ",
              "ARS : 0.82",
              "HNL : 0.17",
              "AUD : 1.9622",
              "MAD : 0.208"]
for rate in currencies:
    rates.writelines(rate+"\n")
rates.close()
rates = open("rates.txt", "r")
text = rates.readlines()
for i in text:
    word, number = i.split(":")[0], i.split(":")[1].rstrip("\n")
    print(f"I will get {round(n_conicoins * float(number),2)} {word}from the sale of {n_conicoins} conicoins.")