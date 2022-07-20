# answer 1
n = int(input("enter the number:"))
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev*10 + dig
    n = n / 10

if temp == rev:
    print("number is palindrome")
else:
    print("number is not palindrome")

# answer 2
print("###############################")
print("answer2")
num = int(input("enter a number to find a factorial"))
def factorial(a):
    if a == 1 or a == 0:
        return 1
    else:
       return a * factorial(a-1)


print(factorial(num))
# answer3
print("###############################")
print("answer 3")


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


num = int(input("how many numbers"))
if num <= 0:
    print("please enter the right number")
else:
    print("print fibonacci series")
    for i in range(num):
        print(fibonacci(i))

# answer 4
print("########################################")
print("answer 14")
print("Armstrong Number checking:")
sum = 0
num = int(input("enter the number to check whether it is armstrong or not"))
print(num)
order = len(str(num))
original_num = num
while num > 0:
    digit = num % 10
    sum = sum + digit ** order
    num = num // 10
if sum == original_num:
    print("number is armstrong number")
else:
    print("number is not armstrong number")
    # answer 5
    print("###########################################")
    print("answer 5")


    def add(num1, num2):
        return num1 + num2


    def subtract(num1, num2):
        return num1 - num2


    def multiply(num1, num2):
        return num1 * num2


    def divide(num1, num2):
        return num1 / num2


    print("Please select operation -\n"
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n")

    select = int(input("Select operations form 1, 2, 3, 4 :"))

    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if select == 1:
        print(number_1, "+", number_2, "=",
              add(number_1, number_2))

    elif select == 2:
        print(number_1, "-", number_2, "=",
              subtract(number_1, number_2))

    elif select == 3:
        print(number_1, "*", number_2, "=",
              multiply(number_1, number_2))

    elif select == 4:
        print(number_1, "/", number_2, "=",
              divide(number_1, number_2))
    else:
        print("Invalid input")
# answer 6
"""print("######################################")
print("answer 6")
print("Patterns in python :")
for x in range(10):
    print(x)
print("Simple pyramid pattern :")
for x in range(4):
    for y in range(0,x+1):
        print("*",end="")
    print("\r")
print("Square Pattern")
for x in range(4):
    for y in range(4):
        print("*",end="")
    print("\r")"""

# answer 7
print("#######################################")
print("answer 7")
year = int(input("enter the year"))
if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print("year is leap year")
else:
    print("year is not leap year")
# answer 8
print("#########################################")
print("answer 8")
num = int(input("enter any number"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num, "is not a prime number")
        break
else:
    print (num, "is a prime number")
    # answer 9
    print("#####################################")
    print("answer 9")
    print("To calculate area of some figures:")
    print("I.To calculate area of triangle:")
    print("(a)With three sides")
    # formula = (s*(s-a)(s-b)(s-c))**0.5 where s = (a+b+c)/2
    a = float(5)
    b = float(6)
    c = float(9)
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('The area of traingle is' '%0.2f' % area)
    print("(b)With two sides")
    a = float(15)
    b = float(10)
    area = a * b * 1 / 2
    print(area)
    print("II.To calculate area of rectangle:")
    a = float(15.2)
    b = float(0.5)
    area = a * b
    print(area)
    print("III.To calculate area of sqaure:")
    a = float(20)
    area = a ** 2
    print(area)
    # answer 10
    print("##########################################")
    print("answer 10")
    print("to reverse a list:")
    l = [1, 56, 87, 12]
    print(l)
    l.reverse()
    print(l)
    print()
    # answer 11
    print("############################################")
    print("answer 11")
    print("To find sum of all elements of a list:")
    l = [20, 1, 35, 37]
    sum = 0
    for i in range(0, len(l)):
        sum += l[i]
    print(sum)
    print()
    # answer 12
    print("#############################################")
    print("answer 12")
    print("To find min,average,max of a list:")
    l = [54, 80, 1, 10, 106]
    print(l)
    print("minimum element in a list is ", min(l))
    print("maximum element in a list is ", max(l))
    print("length=", len(l))
    sum = 0
    for i in range(0, len(l)):
        sum += l[i]
    print("sum=", sum)
    print("average element in a list is ", sum / len(l))
    # answer 13
    print("#####################################")
    print("answer 13")
    def grouping_dictionary(l):
        result = {}
        for k, v in l:
            result.setdefault(k, []).append(v)
        return result


    colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    print("Original list :")
    print(colors)
    print("\n Grouping a sequence of key value pair:")
    print(grouping_dictionary(colors))

    # answer 14
    print("##########################################")
    print("answer 14")


    def nested_dictionary(l1, l2, l3):
        result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
        return result


    student_section = ["Yashan", "chirag", "Yuvraj", "raunak"]
    student_name = ["C2", "C1", "C2", "C3"]
    student_marks = [85, 98, 89, 92]
    print("Original strings:")
    print(student_section)
    print(student_name)
    print(student_marks)
    print("\nNested dictionary:")
    print(nested_dictionary(student_section, student_name, student_marks))
# answer 15
print("##########################################")
print("answer 15")
my_set = {3, 4, 6}
my_set2 = {3, 4, 3, 6, 2, 4}
print(my_set.issubset(my_set2))

# answer 16
print("##########################################")
print("answer 16")
my_set3 = {4, 9, 1, 6, 2, 0}
my_set4 = {5, 9, 6, 3}
print(my_set3.difference(my_set4))
# answer 17

print("##########################################")
print("answer 17")
def remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
tuples=[(),(),('a','b'),('a','b','c'),(','),("d")]
print(remove(tuples))

# answer 19
print("##########################################")
print("answer 19")
print("To check validity of password:")
l, u, d, s = 0, 0, 0, 0
Password = 'ritesh6^'
lowercase_alphabets = 'asdfghjklpoiuytrewqzxcvbnm'
uppercase_alphabets = 'ASDFGHJKLPOIUYTREWQZXCVBNM'
digits = "0123456789"
specialchar = '!@#$%^&*'
if len(Password) >= 6:
    for i in Password:
        if i in lowercase_alphabets:
            l += 1
        if i in uppercase_alphabets:
            u += 1
        if i in digits:
            d += 1
        if i in specialchar:
            s += 1
if l >= 1 and u >= 1 and d >= 1 and s >= 1 and l+u+d+s == len(Password):
    print("Password is valid")
else:
    print("Password is  not valid")