class Seat:
    def __init__(self, row, col, id):
        self.row = row
        self.col = col
        self.id = id

def getPos(dir, seats):
    if len(dir) == 1:
        if dir[0] == 'F' or dir[0] == 'L':
            return seats[0]
        if dir[0] == 'B' or dir[0] == 'R':
            return seats[1]

    if dir[0] == 'F' or dir[0] == 'L':
        return getPos(dir[1:], seats[:int(len(seats)/2)])
    if dir[0] == 'B' or dir[0] == 'R':
        return getPos(dir[1:], seats[int(len(seats)/2):])

seatsAll = list()
codeList = list()

with open("input.txt","r") as file:
    for line in file:
        codeList.append(line) 


for elem in codeList:
    tmp_row = getPos(elem[:7],[num for num in range(0,128)])
    tmp_col = getPos(elem[7:-1],[num for num in range(0,8)])
    tmp_id  = tmp_row * 8 + tmp_col

    seatsAll.append(tmp_id)

print("Max ID: "+ str(max(seatsAll)))

takenSeats = sorted(seatsAll)

for i in range(len(takenSeats)):
    if takenSeats[i]+1 != takenSeats[i+1]:
        print("My ID: " + str(takenSeats[i]+1))              
        break