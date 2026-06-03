#Simple interest calculator.

print("=============THE ULTIMATE CALCULATOR=============")
def taking_input():#INPUT BLOCK FOR THE NORMAL CALCULATOR.
    while True:
        try:      
            F = float(input("\nEnter your first Number: "))
            S = float(input("\nEnter your second Number: "))
            return F, S
        except ValueError:
            print("\nEnter a valid number.....(again try using your 🧠)")
            continue
def normal():#CALCULATION BLOCK..
    while True:
        try:
           print("\n1.Addition.")
           print("2.Substraction.")
           print("3.Multiplication.")
           print("4.Division.")
           print("5.To return to menu.")

           action = int(input("\nChoose the operation from above list[1 to 5]: "))
        
        except ValueError:
            print("\nEnter a valid input....try using integers or (your 🧠❗)")
            continue
            
        if action==1:
            print("\noperation addition....🧐")
            F, S = taking_input()
            print("=====RESULT====:",F + S)
        elif action==2:
            print("\noperation addition....🧐")
            F, S = taking_input()
            print("=====RESULT====:",F - S)
        elif action==3:
            print("\noperation addition....🧐")
            F, S = taking_input()
            print("=====RESULT====:",F * S)
        elif action==4:
            print("\noperation addition....🧐")
            F, S = taking_input()
            print("=====RESULT====:",F / S)
        else:
            print("Press Enter to return to the main MENU...")
            menu()
def calculate():  # SIMPLE INTEREST block.
    while True:
        print("\n😎.Calculating Simple Interst.")
        print("")   
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
    print("\nPress 5 to return to the main menu...")
    menu()
def menu():  # MENU block.
    while True:
        print("\nMENU")
        print("\n1.Normal calculator.")
        print("\n2.simple interest.")  # calculates the interest from the users data.
        print("\n3.exit.")
        try:
            action = int(input("\nChoose the tool you need: "))
        except ValueError:
            print("\nInvalid input...try integers.(if you have 🧠!)")
            continue
        if action == 1:
            normal()
        elif action == 2:
            calculate()
        elif action == 3:
            print("Exiting....")
            break
        else:
            print("Enter valid operation...")
menu()
#End of the code!