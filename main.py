#Simple interest calculator.

print("=============THE SIMPLE INTEREST CALCULATOR=============")

def calculate():
    P = float(input("\nEnter your Principle: "))
    R = float(input("\nEnter your rate: "))
    T = float(input("\nEnter your time: "))
    
    interest = (P*T*R)/100
    total_amount = P + interest

    print("\n========RESULTS========")
    print(f"Calculated interest: {interest}")    
    print(f"Total amount: {total_amount}")

def menu():
    print("\n=============select what you want to perform")
    print("\n1. To calculate simple interest")
    print("\n2. To exit")
    
    while True:
        action = int(input("\nEnter what you want to perform: "))

        if action == 1:
            calculate()
        elif action ==2:
            exit()
        else:
            print("invalid input")
menu()

