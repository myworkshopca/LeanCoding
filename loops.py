upto = int(input("Set the upto number: "))
# set the variable to go through all numbers from 1 to 100
i = 1
# set the vaiable to store the sum.
total = 0

while True:
  total = total + i
  # print("i = {1}, total = {0}".format(total, i))
  #i = i + 1
  i += 1
  if i > upto:
    break

print("i = {1}, total = {0}".format(total, i))