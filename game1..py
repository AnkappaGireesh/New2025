#Tell computer to select any number
#And make it to lend a number from a friend it's eqaul to already he choosen number and add both
#Take one number from user and add to previous sum..
#Devide the total sum by 2.
#pay back the sum you taken from your friend.
#Finally the remaining is guessed by the user.

from random import *
computer_value=randint(1,1000)
print('The computer selected number:',computer_value)
total=computer_value+computer_value
print('The taken sum by friend is equal to the my value so the sum is:',total)
user_input=int(input('A number given from my side:\n'))
total+=user_input
remain=total/2
remain-=computer_value
attempts=0
while attempts<=5:
 my_guess=int(input('Guess the remaining number!:'))
if remain==my_guess:
   print('I found! The remaining value in you is:\n',my_guess)
   break
else:
   print(f'Sorry try again! your guess{my_guess} is wrong')
   attempts+1
if attempts==0:
  print('your all chance are over')
  print('The remaining number is:',remain)