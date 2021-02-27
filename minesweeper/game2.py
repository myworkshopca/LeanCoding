import curses
import math
import random

# paint field function.
def initfield(center, size):
  
  field = []

  r, c = 0, 0
  for y in range(center[0] - size[0] // 2, center[0] + size[0] // 2):
    field.append([])
    for x in range(center[1] - size[1], center[1] + size[1], 2):
      #stdscr.addstr(y, x, chr(9608))
      field[r].append([y,x,0,"covered"])

    r = r + 1
    # reset column Index

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

def paintfield(stdscr, field, size, colors):

    for r in range(0, size[0]):
        for c in range(0, size[1]):
            paintcell(stdscr, field[r][c], colors)

def colordict():

  curses.start_color()
  curses.use_default_colors()

  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i , -1)

  return {
        "cover": curses.color_pair(9),
        "flag": curses.color_pair(12), # yellow
        "blasted": curses.color_pair(233),
        #"-1": curses.color_pair(16),
        "-1": curses.color_pair(53),
        "0": curses.color_pair(1),
        "1": curses.color_pair(13), # blue
        "2": curses.color_pair(48), # Green
        "3": curses.color_pair(10), # red
        "4": curses.color_pair(52), # 
        "5": curses.color_pair(94), # 
        "6": curses.color_pair(203), # 
        "7": curses.color_pair(90), # 
        "8": curses.color_pair(178), #
  }

def paintcell(stdscr, cell, colors, reverse=False, show=False):
  
  # decide the cell character and cell color
  cell_ch = chr(9608)
  cell_color = colors['cover']

  # check the status of each cell.
  if cell[3] == "flagged":
    cell_ch = chr(9873)
    cell_color = colors['flag']

  if show:
    if cell[2] == -1:
      cell_ch = chr(10041)
      cell_color = colors["-1"]
    else:
      cell_ch = str(cell[2])
      cell_color = colors[str(cell[2])]

  if reverse:
    cell_color = curses.A_REVERSE

  stdscr.addstr(cell[0], cell[1], cell_ch, cell_color)

def flagcell(cell):

  if cell[3] == "flagged":
    cell[3] = "covered"
  elif cell[3] == "covered":
    cell[3] = "flagged"

def digcell():
  return

def opensurrounding():
  return

def sweeper(stdscr):

  curses.curs_set(0)

  sh, sw = stdscr.getmaxyx()
  center = [sh // 2, sw // 2]
  colors = colordict()

  # set this a list [row, column]
  size = [10, 30]

  field = initfield(center, size)
  paintfield(stdscr, field, size, colors)

  r, c = 0, 0
  nr, nc = 0, 0
  # paint the top left cell reverse color.
  paintcell(stdscr, field[r][c], colors, True)
  #stdscr.addstr(field[r][c][0], field[r][c][1], str(field[r][c][2]), curses.A_REVERSE)

  while True:
    userkey = stdscr.getch()
    # 27 ESC, 113 is q
    if userkey in [27, 113]:
      break;
    elif userkey in [curses.KEY_RIGHT]:
      if c < size[1] - 1:
        nc = c + 1
    elif userkey in [curses.KEY_LEFT]:
      if c > 0:
        nc = c - 1
    elif userkey in [curses.KEY_DOWN]:
      if r < size[0] - 1:
        nr = r + 1
    elif userkey in [curses.KEY_UP]:
      if r > 0:
        nr = r - 1
    elif userkey in [102]:
      # flag cell
      flagcell(field[r][c])
    elif userkey in [100]:
      digcell()
    elif userkey in [32]:
      opensurrounding()

    # paint the current cell normally 
    paintcell(stdscr, field[r][c], colors, False)
    # paint the new cell reverse color
    paintcell(stdscr, field[nr][nc], colors, True)
    # reset the current cell row and column id
    r, c = nr, nc

curses.wrapper(sweeper)