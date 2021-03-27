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

# players = ['1234 Sean', '2345 John']

"""
100 x
350 y
349587 u

leaderboard = ['100 x', '350 y', '349587 u']

if score < int(leaderboard[-1].split()[0]):
  username = function that determines your name
  yourscoure = 'score username'
  leaderboard.append(yourscoure)
  sortmethod
"""

for i in range(0, len(players)):
    print(players[i])

if player_score < int(players[-1].split()[0])
# add new player.
players.append("135 Dog")
players.append("35 Cat")

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