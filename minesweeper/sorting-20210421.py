leaders = [
    "Jessica,80",
    "Samuel,90",
    "Sean,136",
    "John,100"
]
print("original:", leaders)

leaders.sort()
print("Sort:", leaders)

leaders.sort(reverse=True)
print("Reverse Sort:", leaders)

def sort_by_len(item):
    return len(item)

def sort_by_score(item):
    player = item.split(',')
    #print(player[1])
    return int(player[1])

leaders.sort(key=sort_by_len)
print("Sort by length:", leaders)

leaders.sort(key=sort_by_score)
print("Sort by Score:", leaders)