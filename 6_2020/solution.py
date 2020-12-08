globalCounter = 0

with open("input.txt","r") as f:
    content = f.read().splitlines()

    i = 0

    while i < len(content):

        chars = set(content[i])
        while content[i] != '':
            tmp_set = set(content[i])
            chars.intersection_update(tmp_set)

            i += 1
            if i >= len(content):
                break
        
        globalCounter += len(chars)
        i += 1

print("Sum: "+str(globalCounter))
