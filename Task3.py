#2.Create a list of size 5 and execute the slicing structure
my_list = [1, 2, 3, 4, 5]
print(my_list[:])

#3.Write a program to get the sum and multiply of all the items in a given list.
list = [11, 5, 17, 18, 23]
total = sum(list)
print("sum of all elements in a given list:",total)
from functools import reduce
list = [11, 2, 4]
result = reduce((lambda x,y: x * y), list)
print("Multiply all elements in given list: ", result)

#4.Find the largest and smallest number from a given list.
NumList = []
Number = int(input("please enter the total number of list elements: "))
for i in range(1, Number + 1):
    value = int(input("please enter the value of %d element: " %i))
    NumList.append(value)

NumList.sort()
print("The smallest element in this list is: ", NumList[0])
print("The largest element in this list is: ", NumList[Number - 1])

#5.Create a new list which contains the specified numbers after removing the even numbers from a defined list.
my_list = [12, 13, 55, 77, 64, 78, 92, 93]
num = [x for x in my_list if x%2!=0]
print(num)

#6.Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and 30 (both included).
my_list = [x**2 for x in range(1,31)]
print(my_list[:5],my_list[-5:])

# 7.Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]
num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)

#8.Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3 = {}
for d in (dict1, dict2): dict3.update(d)
print(dict3)

#9.Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
n=int(input("input a number "))
d = dict()
for x in range(1,n+1):
     d[x]=x*x

print(d)

#10.Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
values = input("input some comma separated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('list : ',list)
print('tuple : ',tuple)
