#Simple interest calculator.
print("=============THE SIMPLE INTEREST CALCULATOR=============")
P = float(input("Enter your interest: "))
R = float(input("Enter your rate: "))
T = float(input("Enter your time: "))
def caculate():
    interest = (P*T*R)/100
    total_amount = P + interest

    print("\n========RESULTS========")
    print(f"Calculated interest: {interest}")    
    print(f"Total amount: {total_amount}")

def menu():
    print("\n=============select what you want to perform")
    print("\n1. To calculate simple interest")
    print("\n2. To exit")

if action = 


