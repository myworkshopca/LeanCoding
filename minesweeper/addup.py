def addup(num):
    if num == 2:
        return 2
    elif num % 2 == 0:
        return num + addup(num - 1)
    else:
        return addup(num - 1)

num = int(input("give a number:"))
print (addup(num))