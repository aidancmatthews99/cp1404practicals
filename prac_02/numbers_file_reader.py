
FILENAME = "numbers.txt"
file_handle = open(FILENAME, "r")
total = 0

data = file_handle.read().split("\n")
for i in range(len(data)):
    total += int(data[i])
print(total)

file_handle.close()

#
# for line in file_handle:
#     total += int(line)
