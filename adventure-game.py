### Down into the mines!! 

input("Do you dare enter the Mines of Doom to seek treasures beyond your comprehension?\n")


# What is the only number spelled out in English with the same number of letters as its value?
# Answer: Four

## Make questions into a dictionary for which path is taken
right_path_questions = {
   "first": "What is the only food that can never go bad?", # Answer: Honey 
    "second": "Which Tasmanian marsupial is known for its temper?", # Answer: Tasmanian Devil
    "third": "What sport has been played on the moon?" # Answer: Golf
}

left_path_questions = {
    "first": "Which metal is associated with the end of the Stone Age?", # Answer: Bronze
    "second": "Which planet has the most moons?", # Answer: Saturn
    "third": "What is the hottest planet in the solar system?" # Answer Venus
}
print(right_path_questions["first"])

def mines_of_doom():
    print("There are two paths for you to choose from. Right or Left.")
    choice = input("Which path do you choose?\n").lower
    if choice == "right":
        print("You travel a ways and enter a large room with a crudely dug hole in the center.")
        

        #
    elif choice == "left":
        print("You travel a winding path and eventually enter a room exactly like the previous one.")
       
        
def right_path():
    print("")
    
    
    
    
def left_path():
    print("")
