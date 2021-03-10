import curses
import random
import math

def debugmsg(stdscr, field, r, c, colors):

    # paint the current cell's values.
    stdscr.addstr(0, 0, str(field[r][c]))

    for sr in [r - 1, r, r + 1]:
        for sc in [c - 1, c, c + 1]:
            # calculate the y and x axis for this cell.
            y = (sr - (r - 1)) + 1
            x = (sc - (c - 1)) * 2
            if (sc < 0 or sc > len(field[0]) - 1 or
                sr < 0 or sr > len(field) - 1):
                stdscr.addstr(y, x, ' ')
                continue
            # surrounding cell
            scell = field[sr][sc]
            if scell[2] == -1:
                ch = chr(10041)
                color = colors['-1']
            else:
                ch = str(scell[2])
                color = colors[ch]

            if sc == c and sr == r:
                color = curses.A_REVERSE
                
            stdscr.addstr(y, x, ch, color)

def initfield(center, size):

    field = []

    r = 0
    # nested loop
    for y in range(center[0] - size[0] // 2, center[0] + size[0] // 2):
        # go through each row.
        field.append([ ])
        for x in range(center[1] - size[1], center[1] + size[1], 2):
            # go through each column of a row
            field[r].append([y, x, 0, "covered"])
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

def paintfield(stdscr, field, size, colors):

    for r in range(0, size[0]):
        for c in range(0, size[1]):
            paintcell(stdscr, field[r][c], colors)

def colordict():

    curses.start_color()
    curses.use_default_colors()

    for i in range(0, curses.COLORS):
        if i == 232:
            # black on red background
            curses.init_pair(i + 1, i, curses.COLOR_RED)
        else:
            # -1 is baack background
            curses.init_pair(i + 1, i, -1)

    return {
        'cover': curses.color_pair(9),
        "flag": curses.color_pair(12), # yellow
        "blasted": curses.color_pair(233),
        #"-1": curses.color_pair(16),
        "-1": curses.color_pair(10),
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

    # block
    cell_ch = chr(9608)
    cell_color = colors['cover']

    if show:
        # decide the cell character and color.
        if cell[2] == -1:
            cell_ch = chr(10041)
        else:
            cell_ch = str(cell[2])

        cell_color = colors[str(cell[2])]
    else:
        if cell[3] == "flagged":
            cell_ch = chr(9873)
            cell_color = colors["flag"]
        elif cell[3] == "revealed":
            cell_ch = str(cell[2])
            cell_color = colors[cell_ch]
        elif cell[3] == "blasted":
            cell_ch = chr(10041)
            cell_color = colors["blasted"]
    
    if reverse:
        cell_color = curses.A_REVERSE

    stdscr.addstr(cell[0], cell[1], cell_ch, cell_color)

def digcell(cell):

    if cell[3] == 'covered':
        if cell[2] < 0:
            cell[3] = 'blasted'
        else:
            cell[3] = 'revealed'

def flagcell(cell):

    if cell[3] == "covered":
        cell[3] = "flagged"
    elif cell[3] == "flagged":
        cell[3] = "covered"

def opensurrounding():
    return

def sweeper(stdscr):

    curses.curs_set(0)

    sh, sw = stdscr.getmaxyx()
    center = [sh // 2, sw // 2]
    colors = colordict()

    size = [20, 30]
    field = initfield(center, size)

    paintfield(stdscr, field, size, colors)

    r, c = 0, 0
    paintcell(stdscr, field[r][c], colors, True)
    debugmsg(stdscr, field, r, c, colors)
    nr, nc = 0, 0

    while True:
        userkey = stdscr.getch()
        # 113 q
        if userkey in [27, 113]:
            break
        elif userkey == curses.KEY_RIGHT:
            if c < size[1] - 1:
                nc = c + 1
        elif userkey == curses.KEY_LEFT:
            if c > 0:
                nc = c - 1
        elif userkey == curses.KEY_DOWN:
            if r < size[0] - 1: 
                nr = r + 1
        elif userkey == curses.KEY_UP:
            if r > 0:
                nr = r - 1
        elif userkey == 100:
            digcell(field[r][c])
        elif userkey == 102:
            # f 102
            flagcell(field[r][c])
        elif userkey == 32:
            opensurrounding()

        # paint the current cell normally
        paintcell(stdscr, field[r][c], colors)
        # the new cell reverse.
        paintcell(stdscr, field[nr][nc], colors, True)
        # reset current cell's index.
        r = nr
        c = nc
        debugmsg(stdscr, field, r, c, colors)

curses.wrapper(sweeper)
#print(initfield([20, 20], [4, 4]))
