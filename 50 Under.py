#This game is between the user and the computer where you keep adding numbers from 1- 20 until either one reaches 50 
#The goal is to get the total numbers from the computer and the user to equal to fifty
#If either one puts a number down that causes the sum to go over 50 then they lose and the other person wins
print("----------50 Under----------")
from random import randint #Import the random integer function from python so the computer can add on to the sum
sum = 0
comp = 0
while sum <= 50:
    user = int(input("Enter a number between 1- 20: ")) #user enters a number
    print ("Your number: ", user)
    sum = sum + user 
    if sum > 50:
        print("\n")
        print("Final total: ", sum)
        print("You lost!")
        print("Computer won!")
    if sum == 50:
        print("\n")
        print("Final total: ",sum)
        print("You won!")
        print("Computer lost!")
    comp = randint(1,20)                 #Using the function "random integers" for the computer to pick a number
    print("Computer number: ", comp) 
    sum = sum + comp 
    if sum > 50:
        print("\n")
        print("Final total: ",sum)
        print("You won!")
        print("Computer lost!")
    if sum == 50:
        print("\n")
        print("Final total: ",sum)
        print("You lost!")
        print("Computer won!")
    continue_ = input("Keep going? y/n") #Ask the user if they want to keep going after they put down a number
    if continue_ == "y":                 #if yes and sum is < 50 then keep going
        if sum < 50:
            print("Total: ",sum)
    if continue_ == "n":                 #if no and sum < 50 then stop and print out the final total and declare the winner
        if sum < 50:
            print("\n")
            print("Final total: ",sum)
            print("You won!")
            print("Computer lost!")
            break                        #break the loop after the sum is over or equal to 50 


