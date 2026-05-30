#Simple interest calculator.

print("=============THE ULTIMATE CALCULATOR=============")

# def normal_calculation():#NORMAL CALCULATION block.
#     print("\n=============CALCULATOR============")
#     print("\nSelect what you want to perform....")
#     print("1.<ADDITION>")
#     print("2.<SUBSTRACTION>")
#     print("3.<MULTIPLICATION>")
#     print("4.<DIVISION>")

#     try:
#         normal = int(input("\nEnter the number respected to operation.."))
#         if normal=="1":
#             print(f"\nAction performed (Addition): {addition}")
            

#     except ValueError:
#         print("Enter a valid input....")
#         return
#     while True:
#         try:
#            F = float(input("\nEnter the first number: "))
#            S = float(input("\nEnter thes second number: "))
#         except ValueError:
#             print("\ninvalid input....Try using integers(if you have 🧠!)")
#             break
                
# def operation()#calculation part.   
#     addition = F + S
#     substraction = F - S
#     multiplication = F * S
#     division = F/S

#     print("\n==========RESULTS==========")
#     print(f"\nAction performed (Addition): {addition}")
#     print(f"\nAction performed (substraction): {substraction}")
#     print(f"\nAction performed (Multiplication): {multiplication}")
#     print

#normal_calculation()  # Removed to prevent immediate execution before menu

def calculate():#SIMPLE INTEREST block.
    while True:   
        try:
           P = float(input("\nEnter your Principal: "))
           R = float(input("\nEnter your rate: "))
           T = float(input("\nEnter your time: "))
           break
        except ValueError:
            print("\nInvalid input...please enter a number...")
            continue

    interest = (P*T*R)/100
    total_amount = P + interest

    print("\n========RESULTS========")
    print(f"Calculated interest: {interest}")    
    print(f"Total amount: {total_amount}")
    
    input("\nPress Enter to return to MENU....")

def menu():#MENU block.
    print("\nMENU")
    print("\n1.Normal calculator.")
    print("\n2.simple interest.")#calulates the interest form the users data.
    print("\n3.exit.")
    
    while True:
        try:
            action=int(input("\nEnter what you want to calculate: "))
        except ValueError:
            print("\nInvalid input...please enter a number! ")
            continue
        if action==1:
            normal_calculation()
        elif action==2:
            calculate()
        elif action==3:
            print("Exiting....")
            break
        else:
            print("Enter valid operation...")
menu()