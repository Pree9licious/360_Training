#1. Write a program in Python to perform the following operation:
#     a)If a number is divisible by 3 it should print “Consultadd” as a string
#     b)If a number is divisible by 5 it should print “Python Training” as a string
#     c)If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
#       string.
for i in range(51):
    if i % 3 ==0 and i % 5==0:
        print("Consultadd-Python Training")
    elif i % 3==0:
        print("Consultadd")
    elif i % 5==0:
        print("Python Training")

#2.Write a program in Python to perform the following operator based task:
#Ask user to choose the following option first:
#If User Enter 1 - Addition
#If User Enter 2 - Subtraction
#If User Enter 3 - Division
#If User Enter 4 - Multiplication
#If User Enter 5 - Average
#Ask user to enter two numbers and keep those numbers in variables num1 and num2
#respectively for the first 4 options mentioned above.
#Ask the user to enter two more numbers as first and second for calculating the average as
#soon as the user chooses an option 5.
#At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
#NOTE: At a time a user can only perform one action.
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)

#5.Write a program in Python which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200.
nl=[]
for x in range(2000, 3000):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print(','.join(nl))

#7.Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#Expected output: 0 1 2 4 5
#Note: Use ‘continue’ statement
for x in range(6):
    if (x==3 or x==6):
        continue
    print(x,end=' ')
print("\n")

#8.Write a program that accepts a string as an input from the user and calculate the number of digits
#and letters.
#Sample input: consul72
#Expected output: Letters 6 Digits 2
s = input("input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("letters",l)
print("digits",d)
#3.Program to implement the given flow chart:
a,b,c=10,20,30
print(a,b,c)
avg = (a+b+c)/3
print("avg=",avg)
if avg > a and avg > b and avg > c:
    print("avg is higher than a,b,c")
else:
    if avg > a and avg > b:
        print("avg is higher than a,b")
    elif avg > a and avg > c:
        print("avg is greater than a,c")
    elif avg > b and avg > c:
        print("avg is greater than b,c")
    elif avg > a:
        print("avg is just greater than a")
    elif avg > b:
        print("avg is just greater than b")
    elif avg > c:
        print("avg is just greater than c")
#6.write the output of following codes.
#1.
x=123
for i in x:
  print(i)
# output:error beacuse int object is not iterable.
#2.
i = 0

while i < 5:
 print(i)
 i += 1
 if i == 3:
     break
 else:
    print("error")
#output:0
#       error
#       1
#       error
#       2
#3.
count = 0

while True:
    print(count)
    count += 1
    if count >= 5:
        Break
#output:0
#       1
#       2
#       3
#       4

#4. Write a program in Python to break and continue if the following cases occurs:
#If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”
num = 1
while num>0:
    print("Good Going")
    num = int(input("enter the no: "))
print("It's over")

#9. Read the two parts of the question below:
#Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.
number =23
user_input =0

while user_input!=number:
    user_input = int(input("guess the lucky number between 1 to 100: "))

#Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)

number = 23
status = True
while status:
    user_input = int(input("guess the lucky number between 1 to 100: "))
    if user_input==number:
        print("Guess is correct")
        status=False
    else:
        print("Your guess is incorrect")
        ans = input("would you like to continue- y or n: ").lower()
        if ans=='y':
            continue
        else:
            break

#10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
#counter=1
#While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
#The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.
counter = 1
correct_num = 45
while counter<=5:
    guess = int(input(f"enter your guess {counter}: "))
    if guess==correct_num:
        print("good guess")
        counter += 1
    else:
        print("please try again")
        counter += 1

print("Game over")

#11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
# the while loop so that users do not have to continue guessing after they found the number. If the user
# does not guess the number at all, print “Sorry but that was not very successful”.
counter =1
correct_num = 45
while counter<=5:
    guess = int(input(f"enter your guess {counter}: "))
    if guess==correct_num:
        print("good guess")
        break
    else:
        print("please try again")
        counter += 1

print("Sorry but that was not very successful")
