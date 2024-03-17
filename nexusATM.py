class Account:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        """Deposit money into the account."""
        self.balance += amount
        self.transaction_history.append(f"Deposited Rs{amount}")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew Rs{amount}")

    def transfer(self, amount, recipient):
        """Transfer money to another account."""
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred Rs{amount} to {recipient}")

    def get_transaction_history(self):
        """Retrieve transaction history."""
        return self.transaction_history

    def display_balance(self):
        """Display the current balance."""
        return f"Your balance is Rs{self.balance}"


def print_nexus_bank_title():
    title = """
   ###########################################################
   #######                                            ########
   #######                NEXUS BANK                  ########
   #######                                            ########
   ###########################################################
"""
    print(title)


def main():
    print_nexus_bank_title()
    print("Welcome to the ATM!")

    # Create accounts
    accounts = {
        'Arryan Patel': Account('1452', 150000),
        'Aditi Naik': Account('1662', 130000),
        'Alex Smith': Account('1256', 140000)
    }

    while True:  # Loop infinitely until quit
        name = input("\nEnter your name: ").title()
        if name in accounts:
            pin = input("Enter your PIN: ")
            if pin == accounts[name].pin:
                print(f"Welcome, {name}!")
                atm = accounts[name]

                while True:  # Inner loop for ATM operations
                    print("\nMenu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Transaction History")
                    print("5. Check Balance")
                    print("6. Quit")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        amount = float(input("Enter the amount to deposit: "))
                        atm.deposit(amount)
                        print("Deposit successful.")
                        print(atm.display_balance())  # Display balance after transaction

                    elif choice == '2':
                        amount = float(input("Enter the amount to withdraw: "))
                        atm.withdraw(amount)
                        print(atm.display_balance())  # Display balance after transaction

                    elif choice == '3':
                        amount = float(input("Enter the amount to transfer: "))
                        recipient_name = input("Enter recipient's name: ")
                        if recipient_name in accounts:
                            recipient = accounts[recipient_name]
                            atm.transfer(amount, recipient)
                            print("Transfer successful.")
                            print(atm.display_balance())  # Display balance after transaction
                        else:
                            print("Recipient not found.")

                    elif choice == '4':
                        print("\nTransaction History:")
                        for transaction in atm.get_transaction_history():
                            print(transaction)
                        print(atm.display_balance())  # Display balance after transaction

                    elif choice == '5':
                        print(atm.display_balance())  # Display balance
                            
                    elif choice == '6':
                        print("Thank you for using the ATM. Goodbye!")
                        break

                    else:
                        print("Invalid choice. Please try again.")

                # Inner loop ends, go back to the outer loop
                continue

            else:
                print("Incorrect PIN. Please try again.")
        else:
            print("Account not found. Please try again.")


if __name__ == "__main__":
    main()
