import random
computer_score=0
user_score=0
for a in range(1,5,1):  
     computer_guess=random.randint(0,9)
     user_guess=int(input("enter a guess number"))
     if computer_guess>user_guess:  
          computer_score+=10
          print("computer score is "+str(computer_score))
     elif user_guess>computer_guess:    
        user_score+=10
        print("user score is"+str(user_score))
     elif user_guess==computer_guess:   
         print("no increment")     
     else:
         print("end of game")





