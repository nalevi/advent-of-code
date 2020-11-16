

def generate_int_code(opcodeArr):
	
	idx = 0
	while opcodeArr[idx] != 99:
		if idx % 4 == 0:
			if opcodeArr[idx] == 1:
				opcodeArr[opcodeArr[idx+3]] = opcodeArr[opcodeArr[idx+1]] + opcodeArr[opcodeArr[idx+2]]
			elif opcodeArr[idx] == 2:
				opcodeArr[opcodeArr[idx+3]] = opcodeArr[opcodeArr[idx+1]] * opcodeArr[opcodeArr[idx+2]]

			idx += 4
	return opcodeArr


def main(*argc, **argv):
	if argc:
		filename = argv[1]	
	else:
		filename = "input.txt"

	f = open(filename, "r")

	opcodeSeq = f.readline()
	opcodeArr = [int(num) for num in opcodeSeq.split(',')]	
	print("outside: "+str(len(opcodeArr)))

	for i in range(0,99):
		opcodeArr[1] = i
		for j in range(0,99):
			opcodeArr[2] = j
			print("inside: " + str(len(opcodeArr)))
			outArr = generate_int_code(opcodeArr)
			if outArr[0] == 19690720:
				break
			else:
				continue

	if outArr[0] != 19690720:
		print("Nincs m.o")
	else:
		print(str(outArr))

if __name__=="__main__":
	main()
