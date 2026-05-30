#Simple interest calculator.

print("=============THE SIMPLE INTEREST CALCULATOR=============")


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
    print("\n=============select what you want to perform============")
    print("\n1. To calculate simple interest")#calulates the interest form the users data.
    print("\n2. To exit")
    
    while True:
        try:
            action=int(input("\nEnter what you want to perform: "))
        except ValueError:
            print("\nInvalid input...please enter a number! ")
            continue
        if action==1:
            calculate()
        elif action==2:
            print("Exiting....")
            break
menu()