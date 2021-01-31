import curses

def window(stdscr):

  sh, sw = stdscr.getmaxyx()

  # print the welcome mesage.
  msg = "Welcome to my decoding game! Press ESC to exit!"
  stdscr.addstr(0, sw // 2 - len(msg) // 2, msg)

  while True:
    userKey = stdscr.getch()
    stdscr.addstr("ASCII: {0}, Letter: {1}".format(userKey, chr(userKey)))
    if userKey == 27:
      break

curses.wrapper(window)