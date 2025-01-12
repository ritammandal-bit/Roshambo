import random

computer = random.choice([-1,0,1])
youtstr = input("Enter your choice (rock/paper/scissorv): ")
youDict = {"rock":-1,"paper":0,"scissor":1}
reverseDict ={-1:"rock",0:"paper",1:"scissors"}
you = youDict[youtstr]

print(f"\nComputer chose {reverseDict[computer]}\nYour chosed {reverseDict[you]}")

if(computer == you):
    print("That is a draw Game")

else:
    if(computer == -1 and you == 1):
        print("Rock smashes scissors! Computer win!")

    elif(computer ==-1 and you == 0):
        print("Rock coverd paper! you wins!")

    elif(computer == 1 and you == -1):
        print("Rock Broke scissors! you wins!")

    elif(computer == 1 and you == 0):
          print("Scissors cuts paper! Computer wins!")

    elif(computer == 0 and you == -1):
        print("Paper covers rock! Computer win!")

    elif(computer == 0 and you == 1):
        print("Scissors cuts paper! You win!")

    else:
        print("Some thing rong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
