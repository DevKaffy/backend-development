#fileio
filepath = 'file.txt'
file = open(filepath, 'r')
print(file.read())
file.close()
with open(filepath, 'r') as file:
    print(file.read())
# for char in file:
#     print(char)
# print(file.read())