import curses
import random
import math

def initfield(center, size):

    field = []

    r = 0
    # nested loop
    for y in range(center[0] - size[0] // 2, center[0] + size[0] // 2):
        # go through each row.
        field.append([ ])
        for x in range(center[1] - size[1], center[1] + size[1], 2):
            # go through each column of a row
            field[r].append([y, x, 0])
            #stdscr.addstr(y, x, chr(9608))
            #c = c + 1
        r = r + 1
        #c = 0

    # generate the bombs!
    i = 0 # track the bomb count.
    while i < math.prod(size) // 7:
        index = random.randint(0, math.prod(size) - 1)
        # figure out r c
        r = index // size[1]
        c = index - r * size[1]
        if field[r][c][2] == -1:
            continue
        else:
            field[r][c][2] = -1
            i = i + 1

    # calculate the number of bombs.
    for r in range(0, size[0]):
        for c in range(0, size[1]):
            if field[r][c][2] == -1:
                # this cell has bombk
                continue

            for sr in [r - 1, r, r + 1]:
                for sc in [c - 1, c, c + 1]:
                    if sr < 0 or sr >= size[0] or sc < 0 or sc >= size[1]:
                        continue # skip
                    elif sr == r and sc == c:
                        continue # skip
                    else:
                        if field[sr][sc][2] == -1:
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

def colordict():

    curses.start_color()
    curses.use_default_colors()

    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    return {
        'cover': curses.color_pair(9),
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

def sweeper(stdscr):

    curses.curs_set(0)

    sh, sw = stdscr.getmaxyx()
    center = [sh // 2, sw // 2]

    size = [20, 30]
    field = initfield(center, size)

    paintfield(stdscr, field, size)

    r, c = 0, 0
    nr, nc = 0, 0 
    stdscr.addstr(field[r][c][0], field[r][c][1], str(field[r][c][2]), curses.A_REVERSE)

    while True:

        userkey = stdscr.getch()

        if userkey == 29:
            break
        elif userkey == curses.KEY_RIGHT:
            nr = r
            nc = c + 1
        elif userkey == curses.KEY_LEFT:
            nr = r
            nc = c - 1

        # paint the current cell normally
        stdscr.addstr(field[r][c][0], field[r][c][1], str(field[r][c][2]))
        # the new cell reverse.
        stdscr.addstr(field[nr][nc][0], field[nr][nc][1], str(field[nr][nc][2]), curses.A_REVERSE)
        r = nr
        c = nc

curses.wrapper(sweeper)
#print(initfield([20, 20], [4, 4]))
