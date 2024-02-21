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


def mines_of_doom():
    print("There are two paths for you to choose from. Right or Left.")
    choice = input("Which path do you choose?\n")
    print(choice)
    if choice.lower() == "right":
   
      right_path()

        
    elif choice.lower() == "left":
        left_path()
    else:
        print("No choice was made.")
    
        
def right_path():
    print("You travel a ways and enter a large room with a with a spiral staircase that ascends into darkness.")
    print("")
    print("As you ascend the stairs for what seems an eternity you are confronted with a voice that enters your mind")
    print("")
    answer = input(f'{right_path_questions["first"]}\n')
    if answer.lower() == "honey":
        print("Ahh you are correct")
        # answer_two = input(right_path_questions["second"])
    elif answer.lower() != "honey":
        print("You have failed. Now meet your doom!")
        print("The staircase vanishes and you fall into eternal nothingness.")
    
    
    
def left_path():
    print("You follow a winding path and eventually enter a room exactly like the previous one.")
    print("")
    
mines_of_doom()
