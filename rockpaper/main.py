import random

print("welcome to Rock, Paper,Scissors! Press Enter to start")

user_score = 0
cpu_score = 0

while True:
	print()
	user_choice = input("Rock,Paper,or Scissors ").lower()
while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
	   user_choice = input("invalid input, please try again: ").lower()


random_num = random.randint(0,2)
if random_num == 0:
		cpu_choice = "rock"
elif random_num == +1:
		cpu_choice = "paper"
elif random_num == 2:
		cpu_choice = "scissors"

print()
print("your choice:", user_choice)
print("computers choice",cpu_choice)
print()

if user_choice == "rock":
	if cpu_choice == "rock":
			print("it's a tie!")
	elif cpu_choice == "paper":
			print("you lost!")
			cpu_score += 1
	elif cpu_choice == "scissors":
			print("you win")
			user_score += 1
elif user_choice == "paper":
		if cpu_choice == "paper":
			print("it's a tie!")
elif cpu_choice == "scissors":
			print("you lost!")
			cpu_score += 1
elif cpu_choice == "rock":
			print("you win!")
			user_score += 1
elif user_choice == "scissors":
	    if cpu_choice == "scissors":
	     print("it's a tie!")
elif cpu_choice == "rock":
			print("you lost!")
			cpu_score += 1
elif cpu_choice == "paper":
			print("you win!")
			user_score += 1	

print("You have", user_score,"wins")
print("The computer has", cpu_score, "wins")
print()	

repeat = input("Play Again? (Y/N" ).lower()
while repeat != "n" and repeat != "y":
		repeat = input("Invalid input,please try again: ").lower()

if repeat == "n":
    


 print("\n---------\n")


