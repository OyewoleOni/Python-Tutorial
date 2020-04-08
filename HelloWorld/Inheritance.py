class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass


cat = Cat()
cat.walk()
dog = Dog()
dog.walk()