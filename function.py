import random

def greeting(name):
  print("Hi {0}, How are you?".format(name))

def sum(number_list):
  total = 0
  for num in number_list:
    total += num

  return total

#print(sum([2,3,4,5,100,23]))

print(random.randint(0, 10))

while True:
  a = random.randint(0, 100)
  print(a)
  if a == 8:
    break