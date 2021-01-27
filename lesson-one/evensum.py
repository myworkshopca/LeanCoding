greeting = """
****************************
* Welcome to event number  *
****************************
"""
print(greeting)

# set the variable to track the number.
# starts from 1
i = 1
# set the variable to sore the sum
# set it start from 0
total = 0
# set up the while loop to go through each number.
while i <= 100:
  # check if i is a even number or odd number.
  if i % 2 == 0:
    # i is an event, add it to total.
    total = total + i
    i = i + 1
  else:
    # i is an odd number
    i = i + 1

# show the total
print("Total of event number: ", total)