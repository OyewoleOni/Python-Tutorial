numbers = [5, 2, 5, 2, 2]
numbers.append(20)
print(numbers)

numbers.insert(0, 10)
print(numbers)

numbers.remove(10)
print(numbers)

numbers.pop()
print(numbers)

print(50 in numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)