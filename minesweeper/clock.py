import curses
import datetime

def clock(stdscr):

    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(50)

    start_time = datetime.datetime.now()

    while True:
        userkey = stdscr.getch()

        if userkey in [27, 113]:
            break
        elif userkey == 32:
            stdscr.nodelay(False)
            stdscr.timeout(-1)
            
            # turn on the cursor
            curses.curs_set(1)
            stdscr.addstr(10, 0, 'Type your name: ')
            name = ''
            while True:
                userinput = stdscr.getch()
                if userinput == 10:
                    stdscr.addstr(5, 0, name)
                    # resume...
                    curses.curs_set(0)
                    stdscr.nodelay(True)
                    stdscr.timeout(50)
                    break
                else:
                    name = name + chr(userinput)
                    stdscr.addstr(chr(userinput))

        stdscr.addstr(0, 0, str(datetime.datetime.now()))

        stdscr.addstr(3, 0, "Stopwatch: ")
        stdscr.addstr(str((datetime.datetime.now() - start_time).seconds))
        stdscr.addstr(".")
        micors = (datetime.datetime.now() - start_time).microseconds
        stdscr.addstr(str(micors // 100002))

curses.wrapper(clock)