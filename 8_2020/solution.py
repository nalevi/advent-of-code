def main():
   
    instructions = list()
    with open("input.txt","r") as f:
        instructions = f.read().splitlines()

    gIdx = 0
    for gIdx in range(0,len(instructions)):
        tmp_inst = instructions
        tmp_val = tmp_inst[gIdx]

        if tmp_val.split(' ')[0] == "nop":
            tmp_inst[gIdx] = "jmp " + tmp_val.split(' ')[1]
        elif tmp_val.split(' ')[0] == "jmp":
            tmp_inst[gIdx] = "nop " + tmp_val.split(' ')[1]

        accumlator = 0
        idx = 0
        prevInst = list()

        while prevInst.count(idx) != 1:
            prevInst.append(idx)

            if tmp_inst[idx].split(' ')[0] == "nop":
                idx += 1
            elif tmp_inst[idx].split(' ')[0] == "acc":
                accumlator += int(tmp_inst[idx].split(' ')[1])
                idx += 1
            elif tmp_inst[idx].split(' ')[0] == "jmp":
                idx += int(tmp_inst[idx].split(' ')[1])
            
            if idx >= len(instructions):
                print("The value: " + str(accumlator))
                break



if __name__=='__main__':
    main()