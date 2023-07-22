def main():
    print("This program converts US Dollars into Pound Sterling")
    print()

    dollars=eval(input("Enter the amount: "))
    pounds=convert_to_pounds(dollars)
    print("That is",pounds,"pounds.")

convert_to_pounds = lambda dollars: dollars*0.82
main()