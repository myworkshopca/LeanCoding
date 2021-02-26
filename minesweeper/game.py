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

def sweeper(stdscr):

    sh, sw = stdscr.getmaxyx()
    center = [sh // 2, sw // 2]

    size = [20, 30]
    field = initfield(center, size)

    paintfield(stdscr, field, size)

    stdscr.getch()

#curses.wrapper(sweeper)
print(initfield([20, 20], [4, 4])
