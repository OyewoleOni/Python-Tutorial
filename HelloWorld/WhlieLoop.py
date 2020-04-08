i = 1
while i <= 5:
    print("*" * i)
    i +=1
print("Done")

secret_number = 9
guessCount = 0
guess_limit = 3
while guessCount < guess_limit:
   guess= int(input("Guess: "))
   guessCount +=1
   if guess == secret_number:
       print("You won!")
       break
else:
    print("Sorry you failed!")



