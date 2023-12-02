# Part 2

with open('Day 2 Input.txt', 'r') as file:
  game_sum = 0
  for line in file:
    game += 1
    red = 0
    blue = 0
    green = 0
    num = 0
    double_digit = True
    string = [*line]
    string.pop(5)
    string.append("<")
    while string[0] != "<":
      flag = True
      try:
        int(string[0])

      except ValueError:
        flag = False

      if not flag:
        if string[0] == 'r':
          if num > red:
            red = num
          for i in range(3):
            string.pop(0)
        elif string[0] == 'g':
          if num > green:
            green = num
          for i in range(5):
            string.pop(0)
        elif string[0] == 'b':
          if num > blue:
            blue = num
          for i in range(4):
            string.pop(0)
        else:
          string.pop(0)
        flag = True
      elif flag:
        try:
          int(string[1])

        except ValueError:
          double_digit = False

        if double_digit:
          num = (int(string[0]) * 10) + int(string[1])
          for i in range(2):
            string.pop(0)
        elif not double_digit:
          num = int(string[0])
          string.pop(0)
          double_digit = True

    game_sum += (red * blue * green)

print('Sum of Games: ' + str(game_sum))
