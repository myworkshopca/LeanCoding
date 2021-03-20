import curses

def clock(stdscr):

    curses.curs_set(0)
    #stdscr.nodelay(False)
    #stdscr.timeout(50)

    #file = open("leaderboard", "w")
#
    #file.write("Hello one file!\n")
    #file.write("Hello file!")
    #file.close()

    # read content from a file
    rf = open("minesweeper/leaderboard", "r")
    content = rf.read()
    players = content.split("\n")
    for player in players:
        score = player.split(',')
        stdscr.addstr(str(score[0]) + "====")
    
    userkey = stdscr.getch()

curses.wrapper(clock)