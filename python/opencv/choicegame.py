from random import randint
import os
playerscore = 0
computerscore = 0

def playAgain():
    print('*********************************************')
    print("Do you want to play again? (Select Y or N)")
    return input().lower().startswith('y')

def getFullString(strng):
    dict_options = {'r':'Rock','s':'Scissors','p':'Paper'}
    for k, v in dict_options.items():
        if k == strng:
            return v
def getScore():
    print('***************Score*******************')
    print("Computer = ",computerscore)
    print("Player = ",playerscore)    
    print('*********************************************')
        
while playAgain():
    os.system('cls')
    print("Enter your choice. Choose R for Rock, P for Paper or S for Scissors")
    player1 = input().lower()
    print('*********************************************')
    if (player1 != 'r' and player1 != 'p' and player1 != 's'):
        print ("Choose R for Rock, P for Paper or S for Scissors")
    else:    
        randnum = randint(1,3)
        if randnum==1:
            computer = 'r'
        elif randnum==2:
            computer = 'p'
        else:
            computer = 's'
        print ("You chose " + getFullString(player1))
        print ("Computer chose " + getFullString(computer))
        
        print('*********************************************')
        if (player1 == computer):
            print ("It's a tie!")
        elif (player1 == 'r' and computer== 'p'):
            print ("Computer Wins!")
            computerscore = computerscore+1
        elif (player1 == 'p' and computer== 's'):
            print ("Computer Wins!")
            computerscore = computerscore+1
        elif (player1 == 's' and computer== 'r'):
            print ("Computer Wins!")
            computerscore = computerscore+1
            
        elif (player1 == 'r' and computer== 's'):
            print ("Congratulations! You Win!")
            playerscore = playerscore+1
        elif (player1 == 'p' and computer== 'r'):
            print ("Congratulations! You Win!")
            playerscore = playerscore+1
        elif (player1 == 's' and computer== 'p'):
            print ("Congratulations! You Win!")
            playerscore = playerscore+1
        getScore()
        print ("\n" * 10)