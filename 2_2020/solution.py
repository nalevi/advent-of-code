
file = open("input.txt","r")

passwords = list()

for line in file:
    passwords.append([line.split(":")[0], line.split(":")[1]])

file.close()

validpw = 0

"""
part 1:

for elem in passwords:
    if elem[1][1:-1].count(elem[0].split(' ')[1]) in range(int(elem[0].split(' ')[0].split('-')[0]),int(elem[0].split(' ')[0].split('-')[1])+1):
        validpw += 1
"""


#part 2:
for elem in passwords:

    first = False
    second = False

    if elem[1][:-1][int(elem[0].split(' ')[0].split('-')[0])] == elem[0].split(' ')[1]:
        first = True

    if elem[1][:-1][int(elem[0].split(' ')[0].split('-')[1])] == elem[0].split(' ')[1]:
        second = True

    if first and not second:
        validpw += 1
    elif not first and second:
        validpw += 1

print("Valid passwords count: " + str(validpw))