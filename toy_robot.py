class ToyRobot:
  def __init__(self, x, y):
    self.x = None
    self.y = None
    self.direction= None

    self.max_x = x
    self.max_y = y
  
    self.accept_input()
  
  def validate_place(self, user_input):
    user_input = user_input[5:].split(',')
    try:
      self.x = int(user_input[0])
      self.y = int(user_input[1])
      self.validate_direction(user_input[2].strip().upper())
    except:
      print("Invalid command. Please try again.\n")
  
  def validate_direction(self, direction):
    if direction not in ['NORTH', 'SOUTH', 'WEST', 'EAST']:
      print("Invalid direction. Please try again.\n")
    else:
      self.direction = direction

  def accept_input(self):
    """
    Accept input from user
    """
    user_input = input()
    if 'PLACE' in user_input:
      self.validate_place(user_input)
    elif not self.direction:
      print("Invalid command. Please try again.")
    elif user_input.upper() == 'MOVE':
      self.move_robot()
    elif user_input.upper() == 'LEFT':
      if self.direction == 'NORTH':
        self.direction = 'WEST'
      elif self.direction == 'EAST':
        self.direction = 'NORTH'
      elif self.direction == 'WEST':
        self.direction = 'SOUTH'
      elif self.direction == 'SOUTH':
        self.direction = 'EAST'
    elif user_input.upper() == 'RIGHT':
      if self.direction == 'NORTH':
        self.direction = 'EAST'
      elif self.direction == 'EAST':
        self.direction = 'SOUTH'
      elif self.direction == 'WEST':
        self.direction = 'NORTH'
      elif self.direction == 'SOUTH':
        self.direction = 'WEST'
    elif user_input.upper() == 'REPORT':
      print("Current position of robot: ",
            self.x,
            self.y,
            " and robot is facing :",
            self.direction)
      return self.display_menu()
    else:
      print("Invalid command. Please try again.\n")
    return self.accept_input()

  def move_robot(self):
    if self.direction == 'NORTH' and (0 <= (self.y + 1) < self.max_y):
      self.y += 1
    elif self.direction == 'EAST' and (0 <= (self.x + 1) < self.max_x):
      self.x += 1
    elif self.direction == 'WEST' and (0 <= (self.x - 1) < self.max_x):
      self.x -= 1
    elif self.direction == 'SOUTH' and (0 <= (self.y - 1) < self.max_y):
      self.y -= 1
    else:
      print("Invalid Move")

  def display_menu(self):
    """
    Display menu
    """
    user_input = input("Do you want to continue ? (y/n) : ") 
    if user_input.lower() == "y":
      self.accept_input()
    else:
      print("Thank You... ")

if __name__ == "__main__":
  print("\t" * 4 + "Toy Robot Simulator")
  print("Please enter commands to move rebot:\n")
  ToyRobot(5, 5)
