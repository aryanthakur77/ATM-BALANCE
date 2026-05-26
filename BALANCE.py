balance = 10000
transactions = []


def display_balance():
    print("Balance =", balance)


def deposit():
    global balance

    amount = int(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited {amount}")
        print("Money Deposited")
    else:
        print("Invalid Amount")


def withdraw():
    global balance

    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient Balance")

    elif amount <= 0:
        print("Invalid Amount")

    else:
        balance -= amount
        transactions.append(f"Withdrawn {amount}")
        print("Money Withdrawn")


def statement():

    if len(transactions) == 0:
        print("No Transactions")

    else:
        print("\nTransaction History:")

        for i in transactions:
            print(i)


while True:

    print("""
1. Display Balance
2. Deposit Money
3. Withdraw Money
4. Statement
5. Exit
""")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        statement()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")