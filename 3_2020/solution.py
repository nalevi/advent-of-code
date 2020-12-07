file = open("input.txt","r")
table = list()

for line in file:
    row = list()
    for ch in line:
        if ch != '\n':
            row.append(ch)
    
    table.append(row)

file.close()


steps = [[1,1],[3,1],[5,1],[7,1],[1,2]]
tableSize = len(table)
allTrees = 1

for stp in steps:
    treeCounter = 0
    i = 0
    j = 0
    while i != tableSize-1:
        
        if (len(table[i])-1) < (j+stp[0]):
            for k in range(i, tableSize):
                table[k] += table[k]

        j += stp[0]
        i += stp[1]

        if table[i][j] == '#':
            treeCounter += 1

    allTrees *= treeCounter

print("Vége: " + str(allTrees))

