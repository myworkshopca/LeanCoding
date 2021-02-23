import curses
import math
import random

# paint field function.
def initfield(center, size):
  
  field = []

  r, c = 0, 0
  for y in range(center[0] - size[0] // 2, center[0] + size[0] // 2):
    field.append([[0]] * size[1])
    for x in range(center[1] - size[1], center[1] + size[1], 2):
      #stdscr.addstr(y, x, chr(9608))
      field[r][c] = [y,x,0]
      c = c + 1
    r = r + 1
    # reset column Index
    c = 0

  #genterate bombs.
  i = 0
  while i < math.prod(size) // 7:
    rand = random.randint(0, math.prod(size) - 1)
    row = rand // size[1]
    column = rand - row * size[1]
    #stdscr.addstr(0,0, str(row))
    if field[row][column][2] == -1:
      continue
    else:
      field[row][column][2] = -1
      i = i + 1

  # calc the number of bombs.
  for r in range(0, size[0]):
      for c in range(0, size[1]):
          # if current cell is bomb.
          if field[r][c][2] == -1:
              continue # skip
          for sr in [r -1, r, r + 1]:
              for sc in [c - 1, c, c + 1]:

                  if sr < 0 or sr > size[0] - 1 or sc < 0 or sc > size[1] - 1:
                      continue # out of field, skip
                  elif sr == r and sc == c:
                      continue # skip
                  elif field[sr][sc][2] == -1:
                      field[r][c][2] = field[r][c][2] + 1

  return field

def paintfield(stdscr, field, size):

    for r in range(0, size[0]):
        for c in range(0, size[1]):
            if field[r][c][2] == -1:
                stdscr.addstr(field[r][c][0], field[r][c][1], chr(10041))
            else:
                #stdscr.addstr(field[r][c][0], field[r][c][1], chr(9608))
                stdscr.addstr(field[r][c][0], field[r][c][1], str(field[r][c][2]))

def sweeper(stdscr):

  sh, sw = stdscr.getmaxyx()
  center = [sh // 2, sw // 2]

  # set this a list [row, column]
  size = [10, 30]

  field = initfield(center, size)
  paintfield(stdscr, field, size)

  stdscr.getch()

curses.wrapper(sweeper)
