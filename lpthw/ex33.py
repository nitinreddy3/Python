# Program to print the numbers until the condition evaluates to false
# Define a empty array
numbers = []

range_val = int(input("Please enter the range of values you want to operate upon: "))
incr_val = int(input("Please enter the increment value you want to operate upon: "))

# A "while" loop to iterate over numbers less than 6 and print the 
# numbers before increment and after increment
def go_while_loop(range_value, incr_value):
    i = 0
    for i in range(0, range_value):
        print("At the top i is %d" % i)
        numbers.append(i)
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

print("The numbers: ")

# Iterate over the numbers to print the list items
for num in numbers:
    print(num)

go_while_loop(range_val, incr_val)

