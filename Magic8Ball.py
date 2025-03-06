#Magic 8 Ball

import time 
import random

time.sleep(1)
name_quest = input("What is your name: ")
time.sleep(1)
user_quest = input("Ask your question: ")

time.sleep(1)

def magicball():
  ball_choice = random.randint(1,10)

  if ball_choice == 1:
    print("Yes for sure!")
  elif ball_choice == 2:
    print("Thas a yes")
  elif ball_choice == 3:
    print("i can't tell you that now")
  elif ball_choice == 4:
    print("Ask later again")
  elif ball_choice == 5:
    print("never ever")
  elif ball_choice == 6:
    print("I don't think so")
  elif ball_choice == 7:
    print("Maybe in the Future")
  else:
    print("Error worng input")

magicball()
