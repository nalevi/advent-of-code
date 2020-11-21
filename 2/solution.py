

def generate_int_code(opcodeArr,noun,verb):
	
	opcodeArr[1] = noun
	opcodeArr[2] = verb
	idx = 0
	while idx < len(opcodeArr):
		if idx % 4 == 0:
			if opcodeArr[idx] == 1:
				opcodeArr[opcodeArr[idx+3]] = opcodeArr[opcodeArr[idx+1]] + opcodeArr[opcodeArr[idx+2]]
				idx += 4
			elif opcodeArr[idx] == 2:
				opcodeArr[opcodeArr[idx+3]] = opcodeArr[opcodeArr[idx+1]] * opcodeArr[opcodeArr[idx+2]]
				idx += 4
			elif opcodeArr[idx] == 99:
				print("Terminate: "+str(opcodeArr[0]))
				break
			else:
				print("unkown code")
				break	

	return opcodeArr


def main(*argc, **argv):
	if argc == 2:
		filename = argv[1]	
	else:
		filename = "input.txt"

	f = open(filename, "r")

	opcodeSeq = f.readline()
	opcodeArr = [int(num) for num in opcodeSeq.split(',')]	

		
	for i in range(100):
		for j in range(100):
			outArr = generate_int_code(opcodeArr,i,j)
			if outArr[0] == 19690720:
				break
		
	#outArr = generate_int_code(opcodeArr,12,2)

	if outArr[0] != 19690720:
		print("Nincs m.o")
	else:
		print(str(outArr[1])+" "+str(outArr[2]))

if __name__=="__main__":
	main()
