import random 

print("")
print("*********************")
print("****   Bagel     ****")
print("*********************")

computer_num = random.randint(100, 200)

player_pick = input("Pick a number between 100-200\n")

if player_pick == computer_num:
    print("You won!")
elif player_pick != computer_num:
#    comp_list =  list(computer_num)
#    player_list = list(player_pick)
   x = 0
   for chr in str(computer_num):
       print(chr)
       print(player_pick[x])
       x = x + 1
# Compare the first digit of each number
# if computer_num[1] == player_pick[1]:


print("Sorry play again.")
print(f"The correct number was {computer_num}.")