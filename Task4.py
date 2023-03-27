#1.Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”
txt = "12abcde456"[::-1]
print(txt)

#2.Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('PriYankaUppAL')

#3.Create a function that takes a list and returns a new list with unique elements of the first list.
def unique_list(numbers):
    unique = []
    for item in numbers :
        if item not in unique:
            unique.append(item)
    return unique

print(unique_list([1, 2, 3, 1, 2]))

#.4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
n=input("enter the string: ")
l=n.split('-')
l.sort()
print('-'.join(l))

#5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
lines = []
while True:
    l = input("enter a string: ")
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)

#6.Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.
def calculateSum (a,b):
	s = int(a) + int(b)
	return s

num1 = "10"
num2 = "20"

sum = calculateSum (num1, num2)

print("Sum = ", sum)

#7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
count1 = 0
count2 = 0
for i in string1:
      count1 = count1 + 1

for j in string2:
      count2 = count2 + 1

if (count1 < count2):
      print ("Larger string is:")
      print (string2)

elif (count1 == count2):
      print ("Both strings are equal.")
else:
      print ("Larger string is:")
      print (string1)

#8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).
sqr_list = []
for i in range(1, 21):
    sqr_list.append(i * i)

print(*sqr_list)

#9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

#11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, list))
print(even_number)

#12. Write a function to compute 5/0 and use try/except to catch the exceptions
def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you are dividing a number by ZERO!!")
except:
    print("Any other exception")

#13.Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
nestedlist = [ [1, 2, 3, 4], ["Ten", "Twenty", "Thirty"], [1.1,  1.0E1, 1+2j, 20.55, 3.142]]
flatlist=[]
for sublist in nestedlist:
    for element in sublist:
        flatlist.append(element)
print(flatlist)

#14.Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.

max_num = 20
n = 1

print("Numbers not divisible by 3 and are multiples of 7")
while n <= max_num:

    if n % 3 != 0 and n % 7 == 0:
        print(n)


    n = n + 1

#15.Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.
def square(n):
    return n*n
my_list = [2,3,4,5,6,7,8,9]
updated_list = map(square, my_list)
print(updated_list)
print(list(updated_list))

#16.what is the output of the codes:
#a)
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
#output:2
#b)
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()