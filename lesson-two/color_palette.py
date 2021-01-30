import curses

def window(stdscr):

  curses.start_color()
  curses.use_default_colors()

  for i in range(0, curses.COLORS):
    curses.init_pair(i +1, i, -1)
    stdscr.addstr("<{0}>".format(i + 1), curses.color_pair(i + 1))

  stdscr.getch()

curses.wrapper(window)