is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely Day")
print("Enjoy your day")

price = 1000000
has_good_credit = True
has_high_income = True
has_criminal_record = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")

if has_high_income and has_good_credit:
    print("Elligible for loan")

if has_high_income or has_good_credit:
    print("Elligible for loan")
if has_good_credit and not has_criminal_record:
    print("Elligible for loan")

temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "J"

if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name must be a maximum of 50 characters")
else:
    print("name looks good")

weight = int(input("Weight: "))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
   converted = weight * 0.45
   print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

