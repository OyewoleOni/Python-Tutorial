numbers = [1, 2, 3, 4, 5, 5, 4, 6]
duplicate_item = numbers[0]

for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)
print(numbers)