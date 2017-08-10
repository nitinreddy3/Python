# Program to print the numbers until the condition evaluates to false

i = 0

# Define a empty array
numbers = []

# A "while" loop to iterate over numbers less than 6 and print the 
# numbers before increment and after increment

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")


# Iterate over the numbers to print the list items

for num in numbers:
    print(num)