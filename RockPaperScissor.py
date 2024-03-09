import random      # 'random module' is imported to use 'random.choice(sequence)' function                                                                                            

print("enter Rock, Paper or Scissor")    # taking user's choice
userChoice = input()


options = ['rock', 'paper', 'scissor']       # taking computer's choice
computerChoice = random.choice(options)
print(computerChoice)

if userChoice not in options:       # cheking wether user's choice is valid or not
    print("Invalid choice!")


if userChoice ==  computerChoice:
    print("Draw match")

elif userChoice == 'Paper' and computerChoice == 'rock':
    print("user wins")

elif userChoice == 'rock' and computerChoice == 'scissor':
    print("user wins")

else:
    print("computer wins")


