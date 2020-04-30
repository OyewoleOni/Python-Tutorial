income = float(input("Enter the annual income: "))
max_amount = 85528
fixed_amount = 14839.2

#
# Put your code here.
#

def calculate_tax(income):
    if income < max_amount:
        tax = 0.18 * income - 556.2
        if tax < 0:
            return 0.0
        return round(tax, 0)
    else:
        surplus = (income - max_amount)
        sup = surplus * 32 / 100
        tax = sup +  fixed_amount
        print(income, surplus,sup, tax)
        return round(tax, 0)


tax = calculate_tax(income)
print("The tax is:", tax, "thalers")