# Exercise 1: Print First 10 natural numbers using while loop
# program 1: Print first 10 natural numbers
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2: Print the following pattern
print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")

# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)

# Exercise 4: Write a program to print multiplication table of a given number
n = 2
# stop: 11 (because range never include stop number in result)
# run loop 10 times
for i in range(1, 11, 1):
    # 2 *i (current number)
    product = n * i
    print(product)

# Exercise 5: Display numbers from a list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)

# Exercise 6: Count the total number of digits in a number
num = 75869
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10

    # increment counter by 1
    count = count + 1
print("Total digits are:", count)
# Exercise 7: Print the following pattern
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
# Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)

# Exercise 9: Display numbers from -10 to -1 using for loop
for num in range(-10, 0, 1):
    print(num)
# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done!")
# Exercise 11: Write a program to display all prime numbers within a range
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)
# Exercise 12: Display Fibonacci series up to 10 terms
# first two numbers
num1, num2 = 0, 1

print("Fibonacci sequence:")
# run loop 10 times
for i in range(10):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2

    # update values
    num1 = num2
    num2 = res

# Exercise 13: Find the factorial of a given number
num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

# Exercise 14: Reverse a given integer number
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)

# Exercise 15: Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list[1::2]:
    print(i, end=" ")
# Exercise 16: Calculate the cube of all numbers from 1 to a given number
input_number = 6
for i in range(1, input_number + 1):
    print("Current Number is :", i, " and the cube is", (i * i * i))
# Exercise 17: Find the sum of the series upto n terms
n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)

# Exercise 18: Print the following pattern
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

