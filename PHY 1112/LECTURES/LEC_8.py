split_list = []
master_list = []
for i in range(12):
    for j in range(12):
        split_list.append((i+1) * (j+1))

for i in range(0, len(split_list), 12):
    master_list.append(split_list[i:i+12])

print(master_list)
