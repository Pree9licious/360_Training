# 1.Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type.
a, b, c = "Priyanka", 5.21, 2

#2.Create a variable of type complex and swap it with another variable of type integer.
x = complex(1, 6)
y = 20
print(f"The value of x is {x} and the value of y is {y}")
x, y = y, x
print(f"The new value of x is {x} and y is {y}")

#3(a).Swap two numbers using a third variable.
p = 10
q = 2
r = q
q = p
p = r
print (p,q)
#3(b). Swap two numbers without using a third variable.
d = 3
e = 2
d,e = e,d
print(d,e)

#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
#Version.


#5.Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the
#final output.
print("please enter values between 1-10")
num1 = input('enter first number:'  )
num2 = input('enter second number:')
z = int(num1) + int(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, z))
result = z + 30
print(f'the final output is {result}')

#6.Write a program to check the data type of the entered values.
#HINT: Printed output should say - The data type of the input value is : int/float/string/etc
var = 2.9

if (isinstance(var, float)):
    print("The data type is float")
elif (isinstance(var, int)):
    print("The data type is integer")
elif(isinstance(var, str)):
    print("The data type is string")
else:
    print("please enter valid data type")


#7.Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#UPPERCASE.
a = "PriyankaUppal"
b = "priyankaUppal"
c = "priyanka_uppal"
d = "Priyanka Uppal"

#8.If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?
a = 1
print(a)
a = 2.01
print(a)
a = "priyanka"
# Yes , it will change the value because python supports various data types. It also  accepts different datatype values.
