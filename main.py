#Simple interest calculator.

print("=============THE ULTIMATE CALCULATOR=============")

def normal_calculation():  # NORMAL CALCULATION block.
    print("\n=============CALCULATOR============")
    print("\nSelect what you want to perform....")
    print("1.<ADDITION>")
    print("2.<SUBTRACTION>")
    print("3.<MULTIPLICATION>")
    print("4.<DIVISION>")
    
    try:
        operation_choice = int(input("\nEnter the operation number (1-4): "))
        if operation_choice not in [1, 2, 3, 4]:
            print("\nInvalid operation! Please select 1-4.")
            return
    except ValueError:
        print("Enter a valid input....")
        return
    
    while True:
        try:
            F = float(input("\nEnter the first number: "))
            S = float(input("\nEnter the second number: "))
            break
        except ValueError:
            print("\nInvalid input....Try using numbers!")
            continue
    
    # Perform calculation based on choice
    if operation_choice == 1:
        result = F + S
        operation_name = "Addition"
    elif operation_choice == 2:
        result = F - S
        operation_name = "Subtraction"
    elif operation_choice == 3:
        result = F * S
        operation_name = "Multiplication"
    elif operation_choice == 4:
        if S == 0:
            print("\nError: Cannot divide by zero!")
            input("\nPress Enter to return to MENU....")
            return
        result = F / S
        operation_name = "Division"
    
    print("\n==========RESULTS==========")
    print(f"\nAction performed ({operation_name}): {F} and {S} = {result}")
    print("=============================\n")
    input("\nPress Enter to return to MENU....")

def calculate():  # SIMPLE INTEREST block.
    while True:   
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
            print("\nInvalid input...please enter a number! ")
            continue
        if action == 1:
            normal_calculation()
        elif action == 2:
            calculate()
        elif action == 3:
            print("Exiting....")
            break
        else:
            print("Enter valid operation...")

menu()