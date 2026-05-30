#Simple interest calculator.

print("=============THE ULTIMATE CALCULATOR=============")

def normal():
    while True:
        print("\n1.ADDITION➕")
        print("2.SUBSTRACTION➖")
        print("3.MULTIPLICATION❌")
        print("4.DIVISION➗")





















def calculate():  # SIMPLE INTEREST block.
    while True:
        print("\n😎.Calculating Simple Interst.")   
        try:
            P = float(input("\nEnter your Principal: "))
            R = float(input("\nEnter your rate: "))
            T = float(input("\nEnter your time: "))
            break
        except ValueError:
            print("\nInvalid input...please enter a number...")
            continue

    interest = (P * T * R) / 100
    total_amount = P + interest

    print("\n========RESULTS========")
    print(f"Calculated interest: {interest}")    
    print(f"Total amount: {total_amount}")
    
    input("\nPress Enter to return to MENU....")

def menu():  # MENU block.
    while True:
        print("\nMENU")
        print("\n1.Normal calculator.")
        print("\n2.simple interest.")  # calculates the interest from the users data.
        print("\n3.exit.")
        
        try:
            action = int(input("\nEnter what you want to calculate: "))
        except ValueError:
            print("\nInvalid input...try integers.(if you have 🧠!)")
            continue
        if action == 1:
            Normal()
        elif action == 2:
            calculate()
        elif action == 3:
            print("Exiting....")
            break
        else:
            print("Enter valid operation...")
menu()