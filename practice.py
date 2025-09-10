# to print cube of a number

n = '9'
print(int(n)*int(n)*int(n))

# to print average of numbers

a = "12"
b = "15"
c = "20"
d = "18"
e = "25"
average = (int(a)+int(b)+int(c)+int(d)+int(e)) / 5
print(average)

# a clever problem

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        break
else:
    print("loop")

# Variable declaration to print in different line

a = 10
b = 3.14
c = "A"
d = "true"

print (f"{a}\n{b}\n{c}\n{d}")

# integer to ASCII conversion:

b = int(80)

print(chr(b)) # prints P alphabet

#star pattern triangle by basic method 

print("    *", "   ***", "  *****", " *******", "*********", sep='\n')

# learned something new

a = list(filter(lambda x: x > 3, [1, 2, 3, 4, 5]))
print(a)

# Calculate the Area of a Triangle by giving random input


b = int(input("enter base:"))
h = int(input("enter height:"))
area = 1/2 * b * h
print("area of triangle:", area)

# Adding real and complex numbers with telling it's class type

a = 2 + 3j
b = 4 + 5j
c = a + b
print(a + b)
print(type(c))

#Printing a number is even or odd

num = int(input("enter a number:"))
if num % 2 == 0:
    print("even")
else:
    print("odd")

#Que - Distribution of ticket prices as per different age groups

age = int(input("enter age :"))
if age < 12:
    print("100")
elif age >= 12 and age <= 60:
    print("200")
elif age > 60:
    print("150")

#Que - Grade distribution in a class test according to marks a student has scored

num = int(input("enter your marks:"))
if num >= 90:
    print("A")
elif num >= 75:
    print("B")
elif num >= 60:
    print("C")
elif num < 60:
    print("D")
