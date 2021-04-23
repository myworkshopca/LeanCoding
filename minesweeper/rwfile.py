# override everything.
#f = open('file-one.txt', 'w')
# a will append
file_name = 'file-one.txt'

f = open(file_name, 'w')
leaders = [
    "Jessica,80",
    "Samuel,120",
    "Sean,136"
]
for leader in leaders:
    f.write(leader + '\n');

f.close()

# open a file to read.
f = open(file_name, 'r')
# store the file content in a variable.
content = f.read()
print(content)

