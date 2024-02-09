print("Welcome to spanish")
print("What does 'Nina' mean in spanish?")
print("1. Girl")
print("2. Boy")
print("3. woman")
print("4. man")

intAnswer = int(input("Enter the number of your choice:  "))
if intAnswer == 1: 
    print("You got it right!")
else: 
    print("Sorry you got it wrong, try again.")

    while intAnswer != 1: 
        intAnswer = int(input("Enter the number of your choice: "))
        if intAnswer == 1:
            print("You got it right.")
        else:
            print("sorry you got it wrong, try again.")