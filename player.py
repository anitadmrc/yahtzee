import random
from die import Die
class Player:
  
  def printAllDie(self):
    for i in range(2):
      print(self[i],end="")
      print(", ",end="")
  
    print(self[2])
    
  def __init__(self):
    allDie = [Die(1),Die(2),Die(3)] 
    self.points = 0

  def get_points(self):
    return self.points
  
  def has_three_of_a_kind(self):
    if(self[0]==self[1]):
      if(self[0]==self[2]):
        return True
    return False
  
  def has_pair(self):
    if(self[0]==self[1]):
      return True
  
    elif(self[0]==self[2]):
      return True
  
    elif(self[1]==self[2]):
      return True
    
    else:
      return False
  
  def has_series(self):
    li=sorted(self)
  
    if(li[0].getValue()+1 == li[1].getValue()):
      if(li[0].getValue()+2 == li[2].getValue()):
        return True
    return False
  