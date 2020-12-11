def partOne(arr,summa):
    for i in arr:
        for j in arr:
            if i != j: 
                if i + j == summa:
                    return True

    return False


def partTwo(arr,summa):

    for idx in range(0,len(arr)):
        contList = list()
        contList.append(arr[idx])
        
        for idxInner in range(idx+1,len(arr)):
            
            if sum(contList,0) + arr[idxInner] == summa:
                contList.append(arr[idxInner])
                return min(contList) + max(contList)
            elif sum(contList,0) + arr[idxInner] < summa:
                contList.append(arr[idxInner])
            else:
                break
        

def main():
    data = list()
    with open("input.txt","r") as f:
        data = [int(elem) for elem in f.read().splitlines()]

    idx = 25
    weakPoint = 0                   
    while idx < len(data):
        if not partOne(data[(idx-25):idx], data[idx]):
            weakPoint = data[idx]
        idx += 1

    print(str(partTwo(data,weakPoint)))
        

if __name__=='__main__':
    main()
