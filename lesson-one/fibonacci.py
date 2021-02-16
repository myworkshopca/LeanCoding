# 0,1,1,2,3,5,8,13
# a,b
#   a,b
#     a,b
# set up the variable 
a, b = 0, 1
#a = 0
#b = 1
while a <= 20:
  print(a)
  a, b = b, a + b
  #print(a)