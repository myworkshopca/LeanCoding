import curses

# paint field function.
def initfield(center, size):
  
  field = []

  r, c = 0, 0
  for y in range(center[0] - size[0] // 2, center[0] + size[0] // 2):
    field.append([[0,0,0]] * size[1])
    for x in range(center[1] - size[1], center[1] + size[1], 2):
      #stdscr.addstr(y, x, chr(9608))
      field[r][c] = [y,x]
      c = c + 1
    r = r + 1
    # reset column Index
    c = 0

  return field

def paintfield(stdscr, field, size):

    for r in range(0, size[0]):
        for c in range(0, size[1]):
            stdscr.addstr(field[r][c][0], field[r][c][1], chr(9608))


def sweeper(stdscr):

  sh, sw = stdscr.getmaxyx()
  center = [sh // 2, sw // 2]

  # set this a list [row, column]
  size = [10, 30]

  field = initfield(center, size)
  paintfield(stdscr, field, size)

  stdscr.getch()

curses.wrapper(sweeper)
