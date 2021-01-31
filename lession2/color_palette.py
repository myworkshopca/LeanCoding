import curses

def window(stdscr):

  sh, sw = stdscr.getmaxyx()

  # setup colors.
  curses.start_color()
  curses.use_default_colors()

  # initialize color pairs.
  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, -1)
    stdscr.addstr("<{0}>".format(i + 1), curses.color_pair(i + 1))

  stdscr.getch()

curses.wrapper(window)