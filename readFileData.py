f = open("inputFile.txt", "r")
# print(f.read())

count = 0
for line in f:
    # print(line.split()[1])
    if line.split()[1] == "P":
        print(line)
    count += 1

f.close()
