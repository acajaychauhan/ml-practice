name = input("Operator name: ")
pieces = int(input("Pieces made: "))
rate = float(input("Rate per piece: "))
wage = pieces * rate
print(f"{name} earned Rs {wage:,.2f}")