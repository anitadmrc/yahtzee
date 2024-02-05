import random
class Die:

  def __init__(self, sides):
    self.__num_sides = sides
    self.__value = None

# rolls the die and returns the result
  def roll(self):
    self.__value = random.randint( 1, self.__num_sides )
    
# returns the value of the die
  def getValue(self):
    return self.__value

# allows the die to be set to a selected value
  def setValue(self, val):
    if val > 0 and val <= self.__num_sides:
      self.__value = val
      return True # successfully set the value
    return False; # failed the test

# returns the string representation of the die
  def __str__(self):
    return "D" + str( self.__num_sides ) + " = "+ str( self.__value )

  def __eq__(self, other):
    if self.__value==other.__value:
      return True
    return False

  def __lt__(self, other):
    if self.__value<other.__value:
      return True
    return False

  def __sub__(self, other):
    if self.__value - other.__value:
      return True
    return False