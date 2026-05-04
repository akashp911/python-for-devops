# Tasks:

# Task 1
# Find the number of elements in data using a built-in function.
# Check the data type of data using a built-in function.
# Store both results in variables and print them.

data = ["apple", "banana", "cherry", "date"]
length=len(data)
type=type(data)
print(length)
print(type)

# ##############################################################
# Task 2
# Find the total sum of all numbers using a built-in function.
# Find the largest number in the list using a built-in function.
# Store both results in variables and print them.

numbers = [12, 45, 7, 23, 56, 18]

Total=sum(numbers)
Maximum=max(numbers)

print("sum is:", Total )
print("max number is:", Maximum )



######################################################################

# Find the smallest number using a built-in function.
# Create a new list sorted in ascending order.
# Create another new list sorted in descending order.
# Print all three results.

numbers = [34, 12, 89, 5, 67, 23]

Least=min(numbers)
ascending=sorted(numbers)
decending=sorted(numbers,  reverse=True)

print(Least, ascending, decending)

#########################################
# Find the average of the numbers using built-in functions.
# Print:
# "Average is high" if the average is greater than 25
# "Average is low" otherwise

numbers = [10, 20, 30, 40, 50]

numbers = [10, 20, 30, 40, 50]

Total=sum(numbers)
Length=len(numbers)
average=Total/Length

print("average is:", average)

if average > 25:
    print("average is high")
else:
    print("average is low")
#########################################
# Write a program that:

# Takes a number as input from the user
# Converts it into an integer
# Prints:
# "Even number" if the number is even
# "Odd number" if the number is odd

number = input("Enter a number: ")

number = int(number)

if number % 2 == 0:
  print("Even number")
else:
  print("Odd number")

#########################################
#To get odd number 
num = 7
if num % 2 != 0:
    print(f"{num} is an odd number")
##########################################
# Write a program that:

# Takes two numbers as input from the user (they can be decimals).
# Converts them to float.
# Calculates the difference between the two numbers (larger minus smaller).
# Prints the absolute difference, rounded to 2 decimal places.
# Use float() to convert strings to decimals.
# Use abs() to get the absolute value (always positive).
# Use round(value, 2) to round to 2 decimal places.


number1 = float(input("Enter a number1: "))
number2 = float(input("Enter a number2: "))

difference = abs(number1 - number2)
difference_rounded = round(difference, 2)

print("Absolute difference (rounded):", difference_rounded)
#########################################
# Find the maximum difference between any two numbers in the list.
# Print the result.

numbers = [-20, -5, 10, 25]
difference = max(numbers) - min(numbers)
print("Maximum difference:", difference)

# #########################################
# Find the maximum difference between two numbers such that the larger number comes after the smaller number in the list.
# Print that maximum difference.

numbers = [4, 9, 2, 15, 7, 10]

max_diff = numbers[1] - numbers[0]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        diff = numbers[j] - numbers[i]
        if diff > max_diff:
            max_diff = diff

print("Maximum ordered difference:", max_diff)

#########################################


#########################################

#########################################

#########################################











