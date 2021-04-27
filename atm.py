class ATM(object):
    """
    ATM is a class which has the attributes like pin_check, deposit_amount,
    withdraw_amount, pin_change and so on.
    Some of the attributes are mentioned below
    """
    def __init__(self, name, pin, balance):
        """

        :param name: For entering name
        :param pin: For entering pin
        :param balance: For entering balance amount
        """
        self.name = name
        self.pin = pin
        self.balance = balance

    def pin_check(self, pin):
        """

        :param pin: accepts pin
        :return: checks whether the entered pin is validated or not
        """
        return pin == self.pin

    def __str__(self):
        """

        :return: it returns the account holder's name and the balance amount
        """
        return "{}'s Bank Account with balance {}".format(self.name, self.balance)

    def balance_check(self):
        """

        :return: it checks the balance amount
        """
        return 'Rs' + str(self.balance)

    def deposit(self, dep_amt):
        """

        :param dep_amt: it accepts the amount to be deposited
        :return: updated balance amount
        """
        self.balance += dep_amt

    def withdraw(self, withdraw_amt):
        """

        :param withdraw_amt: it accepts the amount to be withdrawn
        :return: updated balance amount
        """
        try:
            if self.balance >= withdraw_amt:
                if withdraw_amt % 100 == 0:
                    self.balance -= withdraw_amt
        except ValueError:
            print("Insufficient Balance", end="\n")

    def data(self):
        """

        :return: it returns the account holder's name and the balance amount
        """
        return "{},  {}".format(self.name, self.balance)

    def pin_change(self, new_pin):
        """

        :param new_pin: it accepts the new ATM pin to be updated
        :return: the new ATM pin
        """
        self.pin = new_pin


if __name__ == '__main__':
    bank = open("credentials.txt", "r+")
    account_data = bank.read().split(",")
    bank_user = ATM(account_data[0], account_data[1].strip(), int(account_data[2]))
    print("====================WELCOME=====================================")
    print("Welcome " + bank_user.name)


    def savings_transaction():
        """
        It performs savings account operations like deposit, withdrawal, balance_check,
        pin_change etc

        :return: returns the type of savings account transactions selected
        """
        print("================================================================")
        print("Press 1 for deposit")
        print("Press 2 for withdraw")
        print("Press 3 for checking balance")
        print("Press 4 for changing ATM pin")
        print("Press 5 for exit or Exit")
        print("=================================================================")
        choice = int(input("Enter the type of transaction you want to perform : "))
        if choice == 1:
            print("==========================DEPOSIT================================")
            x = input("Enter the amount to be deposited : ")
            bank_user.deposit(int(x))
            print("The updated balance is : " + bank_user.balance_check())
        elif choice == 2:
            print("========================WITHDRAW=================================")
            y = input("Enter the amount to be withdrawn : ")
            bank_user.withdraw(int(y))
            print("Collect your cash")
            print("The updated balance is : " + bank_user.balance_check())
        elif choice == 3:
            print("===========================BALANCE===============================")
            print("The current balance is : " + bank_user.balance_check())
        elif choice == 4:
            print("==========================PIN CHANGE=============================")
            z = input("Enter the new pin : ")
            bank_user.pin_change(z)
            bank.seek(0)
            bank.truncate()
            bank.write(bank_user.data())
        elif choice == 5:
            bank.close()
            exit(1)
        else:
            print("Invalid Input !!!")


    def transactions():
        """
        Current account and savings account operations are performed

        :return: the transactions performed for selected types of account
        """
        while True:
            print("================================================================")
            print("Press 1 for current account")
            print("Press 2 for savings account")
            print("================================================================")
            account = int(input("Enter the type of account : "))
            if account == 1:
                print("================================================================")
                print("You do not have current account.", end="\n")
            else:
                savings_transaction()

            option = input("Do you wish to have another transaction[y/n]?")
            if option == 'y' or option == 'Y':
                savings_transaction()
            elif option == 'n' or option == 'N':
                print("================================================================")
                print("Thank you for banking with us.")
                print("Have a nice day " + bank_user.name + "!!!")
                exit(1)


    print("=========================ENTER PIN==============================")
    for i in range(3):
        pin = input("Enter your  PIN : ")
        print("================================================================")
        if bank_user.pin_check(pin):
            transactions()
            exit(0)
        else:
            if i != 2:
                print("Incorrect PIN. Please enter correct PIN", end="\n")
            else:
                print("Card blocked for 24 hours from now.", end="\n")
                exit(1)
