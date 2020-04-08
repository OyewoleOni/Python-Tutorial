#Exceptions
try:
    age = int(input('age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print(f'age cannot be {age}')
except ValueError:
    print('Invalid Value')