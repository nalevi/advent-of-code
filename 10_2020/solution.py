data = list()
with open("input.txt","r") as f:
    data = [int(num) for num in f.read().splitlines()]


one_diff_counter = 0
three_diff_counter = 0

built_in = max(data) + 3
data.append(built_in)
data.append(0)
data = sorted(data)
#partOne
for idx in range(0,len(data)-1):
    if data[idx] + 1 == data[idx+1]:
        one_diff_counter += 1
    if data[idx] + 3 == data[idx+1]:
        three_diff_counter += 1


print(one_diff_counter*three_diff_counter)

#partTwo
diff_ways = 0
three_diff = 0
two_diff = 0
one_diff = 0
idx = 0

diff_data = [ data[idx+1] - data[idx] for idx in range(0,len(data)-1) ]


while idx < len(data):
    if len(list(filter(lambda x: x == 1, diff_data[idx:idx+4]))) == 4:
        three_diff += 1
        idx += 4
    elif idx + 3 < len(diff_data) and idx > 0 and diff_data[idx-1] == diff_data[idx+3] == 3 and len(list(filter(lambda x: x == 1, diff_data[idx:idx+3]))) == 3:
        two_diff += 1
        idx += 3   
    elif idx + 2 < len(diff_data) and idx > 0 and diff_data[idx-1] == diff_data[idx+2] == 3 and len(list(filter(lambda x: x == 1, diff_data[idx:idx+2]))) == 2:
        one_diff += 1
        idx += 2
    elif idx + 3 < len(diff_data) and idx == 0 and diff_data[idx+3] == 3 and len(list(filter(lambda x: x == 1, diff_data[idx:idx+3]))) == 3:
        two_diff += 1
        idx += 3   
    elif idx + 2 < len(diff_data) and idx == 0 and diff_data[idx+2] == 3 and len(list(filter(lambda x: x == 1, diff_data[idx:idx+2]))) == 2:
        one_diff += 1
        idx += 2
    else:
        idx += 1

print()
print(three_diff)
print(two_diff)
print(one_diff)
print(pow(7,three_diff)*pow(4,two_diff)*pow(2,one_diff))

