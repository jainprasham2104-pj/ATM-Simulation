print("ATM Simulation System")

balance = 5500

while True:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))

            if amount > 0:
                balance += amount
                print("Deposit Successful")
                print("Updated Balance:", balance)
            else:
                print("Enter a valid amount")

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance")

        elif choice == 4:
            print("Thank You For Using ATM")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter numbers only")