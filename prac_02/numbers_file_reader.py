
FILENAME = "numbers.txt"
file_handle = open(FILENAME, "r")
total = 0

data = file_handle.read().split("\n")
for line in data:
    total += int(line)
print(total)

file_handle.close()

#
# for line in file_handle:
#     total += int(line)
