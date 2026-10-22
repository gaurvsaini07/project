#q1

#r=float(input("the radius of circle is="))
#area=round((2*3.14*r),2)
#print(area)

#q2

# f=int(input("the city temp is in fehrenheit degrees="))
# c=round((f-32)*5/9,2)
# print (c)

#q4     
# import math
# a=math.sqrt(25)
# print(a)



# #q5
# import math
# a=input
# b=input
# c=input


#q6
# a=int("the first side is a")
# b=int("the second side is b")
# c=int("the third side is c")



# string in python 




# s='hello world'
# s.find('1',0,len(s))

# s='jbsdjhbjhbxjchvdchxvj'
# len(s)      


# s="jbjbjczhbxcjhxvjc"
# len(s)
# print(len(s))


# Q1: Write a python program to add all the odd numbers from 0 to 20.


# i = 1
# sum=0
# while i<=20:
#     sum= sum + i
#     i=i+2
# print("sum of all odd numbers between 0 to 20 is: ", sum)

# Q 2: Write a python program to find the sum of all integers greater than 100 and less than 200.

# i = 101
# sum=0
# while i<=200:
#     sum= sum + i
#     i=i+1

# print("sum of all numbers between 100 to 200 is: ", sum)


# Q3: Write a program to display the sum of square of the first ten even natural numbers

# i = 0
# sum=0
# while i<=20:
#     sum= sum + (i*i)
#     i=i+2

# print("sum of square of the first ten even natural numbers is: ", sum)

#  Q4: Write a python program to display ascii characters from 65 to 90

# i = 65
# while i<=90:
#     print( chr(i),'=',i)
#     i=i+1

#Q5Display ascii characters from 48 to 57.
# i=48
# while i<=57:
#     print(chr(i),"=", i)
#     i=i+1

#Q6.Display the following output with the help of Ascii character.
# i=97
# while i<=122:
#     print(chr(i) ,"=", i )
#     i=i+1

# Q7: Write a python program for given a Python list you should be able to display Python list in
# the following order
# L1 = [100, 200, 300, 400, 500]
# L1.reverse()
# print(L1)

# Q8: Given a Python list. Write a python program to turn every item of a list into its square
# List1 = [1, 2, 3, 4, 5, 6, 7]

# List1 = [1, 2, 3, 4, 5, 6, 7]

# i = 0

# while i < len(List1):
#     print(List1[i] * List1[i], end=" ")
#     i = i + 1

#Q9: Program to count the number of each vowel in a string.

# List_v=['a','e','i','o','u']

# print(len(List_v))

#Q10: write a Program to sort alphabetically the words form a string provided by the user.
#[You can use split() method to split string into a list of words. ]

# s=str(input("Enter the string: "))
# l = s.split()
# l.sort()
# str = ' '.join(l)
# print(str)


# Q 11: write a Program to Remove Punctuations from a String provided by the user. [Hint: use
# punctuation attribute of string module to get all punctuations (i.e. !&quot;#$%&amp;\&#39;()*+,-
# ./:;&lt;=&gt;?@[\\]^_`{|}~ ) ]
# import string
# punctuations = string.punctuation

# s=input("Enter the string: ")

# cleanStr = ""

# for i in s:
#     if i not in punctuations:
#         cleanStr = cleanStr+ i

# print("string without punctuations is: ", cleanStr)

# Q12: Write a python program to print the Following:
    # 1
    # 2 1
    # 3 2 1

# for i in range(1,4):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

#WAP to print the following asterisk pattern:

# for i in range(1,7):
#     for j in range(1,i+1):
#         print('*', end=" " )
#     print()

#Q14: WAP to create a function traiangle to print the following asterisk triangle pattern:
# for i in range(1,5):
#      for j in range(1,i+1):
#          print('*', end=" " )
#      print()
# for i in range(3,0,-1):
#      for j in range(i,0,-1):
#          print('*', end=" " )
#      print()     



# Q15: Write a python program to print following multiplication table on the screen

for i in range (1,11):
    for j in range (1,11):
        print(i*j,end="\t " )
    print()  
      




