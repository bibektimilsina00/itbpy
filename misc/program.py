# Game

# Generate Random Choise for computer Store in var
# Ask input with user
# compare user chose and computer choise

#game logic

# if computer == user => draw
# elif computer -> rock & user=>paper => user wins
# elif computer -> paper & user=>scissor => user wins
# elif computer -> scissor & user=>rock => user wins

# return result to user



import random









rock ='rock'
scissor="scissor"
paper="paper"

draw="Draw"
win="Win"
loose="Loose"

 


possible_choises=["rock","paper",'scissor',"hammer","pen",'copy','book']

new_list= possible_choises[::-1]
print(new_list)



computer_choise= random.choice(possible_choises)



print(f"possible_choises:     {possible_choises}          ")




user_choise_int= int( input('Input \n 1. rock \n 2. paper \n 3. scissor \n '))


user_game_choise=''

 

if(user_choise_int==1):
    user_game_choise =possible_choises[user_choise_int-1] 
elif(user_choise_int==2):
    user_game_choise=possible_choises[user_choise_int-1]
elif(user_choise_int==3):
    user_game_choise=possible_choises[user_choise_int-1]
 




if (user_game_choise==computer_choise):

    print(f'computer choose {computer_choise } user choose {user_game_choise} so  {draw}')



elif (user_game_choise==rock and computer_choise==scissor ):

    print(f'computer choose {computer_choise } user choose {user_game_choise} so user {win} computer {loose}')
elif (user_game_choise==scissor and computer_choise==paper):
    print(f'computer choose {computer_choise } user choose {user_game_choise} so user {win} computer {loose}')
elif (user_game_choise==paper and computer_choise == rock):
    print(f'computer choose {computer_choise } user choose {user_game_choise} so user  {win} computer {loose} ')

else:
    print(f'computer choose {computer_choise } user choose {user_game_choise} so  computer {win} user {loose} ')















 





 


print(possible_choises)