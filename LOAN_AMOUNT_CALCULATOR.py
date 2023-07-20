import math
def main():
    print("This is the monthly payment calculator")
    print("")
    principal =float(input("Enter the loan amount: "))
    apr=float(input("Enter the annual interest rate: "))
    years=int(input("Enter the no: of years: "))

    monthly_interest_rate=apr/1200
    amount_of_months=years*12
    monthly_payment=principal*monthly_interest_rate/(1-(1+monthly_interest_rate)**(-amount_of_months))
    print(f"The monthly payment for the loan is: {monthly_payment:.2f}")

main()