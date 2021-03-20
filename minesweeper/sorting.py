def sortbythe5thchar(item):
    return item[4]

def sortbyscore(item):
    scores = item.split(",")
    print("sortbyscore: {0}".format(scores))
    return int(scores[0])

# read content from a file
rf = open("minesweeper/leaderboard", "r")
content = rf.read()
players = content.split("\n")

# add new player.
players.append("135,Cat,2021-03-20")
players.append("35,Cat,2021-03-20")

for player in players:
    #player = player.split(',')
    print(str(player))

print("-" * 30)
# sorting.
players.sort(key=sortbyscore)
for player in players:
    #score = player.split(',')
    print(str(player))

# write back to file.