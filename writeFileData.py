f = open("inputFile.txt", "r")
passFile = open("writeFile.txt", "w")
# print(f.read())

count = 0
for line in f:
    # print(line.split()[1])
    passFile.write(line)
    count += 1

f.close()
passFile.close()
