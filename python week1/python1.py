
# Simple ATM Simulator

correct_pin = "1234"
balance = 5000


def login():
    pin = input("Enter your 4-digit ATM PIN: ")

    if pin == correct_pin:
        print("\nLogin successful!")
        return True
    else:
        print("\nIncorrect PIN!")
        return False


def check_balance():
    print(f"\nYour current balance is: ₹{balance:.2f}")


def deposit():
    global balance

    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
        check_balance()
    else:
        print("Please enter a valid amount.")


def withdraw():
    global balance

    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
        check_balance()


def atm_menu():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice! Please try again.")


# Main program
if login():
    atm_menu()
