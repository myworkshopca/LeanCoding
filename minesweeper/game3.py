import curses

def paintfield(stdscr, center, size):

  for y in range(center[0] - size[0] // 2, center[0] + size[0] // 2):
    for x in range(center[1] - size[1], center[1] + size[1], 2):
      stdscr.addstr(y, x, chr(9608))
      

def sweeper(stdscr):

  sh, sw = stdscr.getmaxyx()
  center = [sh // 2, sw // 2]

  size = [6, 12]

  paintfield(stdscr, center, size)

  stdscr.getch()

curses.wrapper(sweeper)