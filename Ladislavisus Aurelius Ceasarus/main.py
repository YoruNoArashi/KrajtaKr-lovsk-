import random
x = random.randint(1,100)
y = input("Do you wanna play? ")
count = 0
if y=="yes"or"Yes"or"ano"or"Ano":
    while y:
        guess = int(input("Guess a number between 1-100: "))
        if x == guess:
            print(f"congrats you've guess the number!, it took you {count} tries")
            break
        elif x<guess:
            print("Try lower....")
            count+=1
        elif x>guess:
            print("Try higher....")
            count+=1
elif y=="No"or"no"or"ne"or"Ne":
    print("kys bozo")