import random
def RPS():
 while True:
  user_action = input("Please enter rock, paper or scissor : ")
  possible_actions = ["rock" , "paper" , "scissor"]
  computer_action = random.choice(possible_actions)

  if user_action == computer_action:
     print(f"Your choice is same as your computer . . . It's a tie!!!")
    
  elif user_action == "rock":
     if computer_action == "scissor":
        print(f"You Won!!! your choice was rock and the computer choice was scissor")
     else:
        print("Paper covers rock! You lose.")

  elif user_action == "paper":
     if computer_action == "rock":
        print(f"You won!!! your choice was rock and the computer choice was rock")
     else:
        print("Scissors cuts paper! You lose.")

  elif user_action == "scissor":
     if computer_action == "paper":
        print(f"You won!!! your choice was scissor and the computer choice was paper")
     else:
        print("Rock smashes scissor. You lose!!!")
        
  play_again = input("Play again? (y/n): ")

  if play_again != 'y':
    break
RPS()
print("Alright, good bye!!!")