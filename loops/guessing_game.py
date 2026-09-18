import random
number=random.randint(1,100)
attempts=0

while True:
    guess=int(input("guess a number from 1 to 100:-"))
    attempts+=1
    if guess==number:
        break
    elif number>guess:
        print("your guess is not correct increase it")
        
    else:
        print("guess is not correct decrease it")

print(f"CONGRATULATIONS!!your guess is correct and your attempts is:-{attempts}")

