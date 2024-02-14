### Down into the mines!! 

input("Do you dare enter the Mines of Doom to seek the treasure?\n")
print("")
print("")

## have one function be game? Don't need each question to be a sepearate function?
def question1():
    print("There are two paths for you to choose from. Right or Left.")
    choice = input("Which path do you choose?\n").lower
    if choice == "right":
        print("You travel a ways and enter a large room with a crudely dug hole in the center.")
        print("")
        input("Do you delve deeper?\n")
        #
    elif choice == "left":
        print("")
    