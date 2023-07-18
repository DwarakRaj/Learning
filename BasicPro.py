
# print("First Program")
# a = int (5)
# b = int (5)
# c =int(a+b)
# print(c)

# while
# i=1
#
#
# while i<=4:
#     print("Dwarak", end =" ")
#     j=1
#     while j<=1:
#         print("Raj", end ="")
#         j=j+1
#     i=i+1
#     print()

# print # 4 times in 4 lines
#
# for i in range(0, 4):
#     for j in range(0,4):
#         print("#", end= '')
#     print("#")

# for i in range(0, 11):
#     print(i)

#isoceles triangle
#for i in range(0, 4):
#     for j in range(0, i):
#         print("*", end= '')
#     print("*")

#Get input & display
# num = int(input("Enter the value"))
# for i in range(0, num):
#     for j in range(0, i):
#         print("*", end= '')
#     print("*")
# isoceles

# for i in range(5):
#     for j in range(i):
#         print("*", end='')
#     print()

#inverse triangle
# for i in range(5):
#     for j in range(5-i):
#         print("*", end='')
#     print()

#numbers
# for i in range(5):
#     for j in range(i+1):
#         print("1", end='')
#     print()

#array in loops - simple way to print array
# from array import *
#
# vals = array('i', [4, 6, 8, 6, 9, 2])
#
# for e in vals:
#     print(e)

#summation or natural numbers

# summation = 0
#
# for j in range(1,9):
#     summation = summation + j
#     print(summation)

#while loop with square
# from array import *
#
# vals = array('i', [4, 6, 8, 6, 9, 2])
#
# newArr = array(vals.typecode, (a*a for a in vals))
#
# i = 0
# while i<len(newArr):
#     print(newArr[i])
#     i+=1

#create empty array, get input, print value of the element using the index

# from array import *
#
# arr = array('I', [])
#
# n = int(input("Enter the length of the array"))
#
# for i in range (n):
#     x = int(input("Enter the next element"))
#     arr.append(x)
# print(arr)
#
# val = int(input("Enter the value for search"))

# k= 0
# for e in arr:
#     if e ==val:
#         print(k)
#         break
#     k+=1

#variable length
# def sum(a, *b):
# 	c=a
# 	for i in b:
# 	    c=c+i
# 	print(c)
# sum(5, 6, 34, 78)

#kwargs - ** it accepts any number of arguments along with key pair

# def person(name, *data):
#     print(name)
#     print(data)
#
# person('Dwarak',25,'Pune',98675)

#double ** with keyworded variable length arg
# def person(name, **data):
#     print(name)
#     for i,j in data.items():
#         print(i, ":", j)
#
# person(name='Dwarak', age=25, city='Pune',Mobile=98675)

#fibonacci series example

# def fib(n):
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range(2, n):
#         c = a+b
#         a = b
#         b = c
#         print(c)
# fib(5)

#factorial

# def name():
#     if ('dwarak' == 'dwarak') and ('raj' == 'raj'):
#         print("Elements are same")
#     else:
#         print("Not same")
# name()

# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))
#
# # first two terms
# n1, n2 = 0, 1
# count = 0
#
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1, "end")
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1
###############################################################
##################### Alphabets##########################
def alphaPattern():
    for i in range(65, 91): print(chr(i), end=" ")
alphaPattern()

########################################





