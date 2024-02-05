#Anita Demirci
#1 March 2023
#The program is a yahtzee game where the user gets a 3 random dice roll at the same time and based on how many pairs they get, the points are calculated.

import random
import check_input
from die import Die
from player import Player
    
def take_turn(self):
  score=0
  print("Rolling Dice... ",end="")
  for i in range(3): #rolls the dice three times
    val=self[i].roll()

  Player.printAllDie(self)

  if(Player.has_three_of_a_kind(self)): #if all of the dice have the same value, player gets three points.
    print("You got 3 of a kind")
    return 3

  elif(Player.has_pair(self)): #if two dice have the same value, player gets one point.
    print("You got a Pair!")
    return 1

  elif(Player.has_series(self)): #if the values of the dice have a sequence, player gets two points.
    print ("You got a Series of 3!")
    return 2
  else: #if all of the values of the dice are different, player gets no point.
    print("Aww. Too Bad")
    return 0

def main():
  print("-Yahtze-")
  player_score =0
  play_again=True

  while play_again: #a while loop that continues until the player quits the game.
    allDie = [Die(1),Die(2),Die(3)] 
    player_score+=take_turn(allDie) #the score value is stored.
    print("Score = "+str(player_score)+" points")
    choice = check_input.get_yes_no("Play Again? (Y/N)")
    if choice == False:
      break
    print("\n")
      
  print("Game over.")
  print("Final Score "+str(player_score)+" points")
      

main()