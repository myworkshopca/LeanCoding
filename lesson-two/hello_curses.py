import curses

def window(stdscr):

  # calculate the center of the window
  # get the height and width of the screen.
  sh, sw = stdscr.getmaxyx()

  msg = "Hello Curses! Type ESC to exit!"
  stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
  # y-axis and x-axis are start from 0 (0, 1)
  stdscr.addstr(sh - 1, 0, str(ord('a')))
  stdscr.addstr(sh - 5, 0, chr(120))

  while True:
    # waiting user's input.
    # getch will return the ascii code, which is a int.
    userKey = stdscr.getch()
    stdscr.addstr(str(userKey))
    stdscr.addstr(chr(userKey))
    if userKey == 27:
      break

curses.wrapper(window)