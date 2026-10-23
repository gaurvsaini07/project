# Q1: Write a Program to make a simple calculator that can add, subtract, multiply and divide
# using functions

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Cannot divide by zero"
#     return a / b


# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))


# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = input("select the operation (1-4): ")

# if choice == '1':
#     print("Result =", add(a, b))
# elif choice == '2':
#     print("Result =", subtract(a, b))
# elif choice == '3':
#     print(f"{a} x {b} = {multiply(a, b)}")
# elif choice == '4':
#     print("Result =", divide(a, b))
# else:
#     print("Invalid choice")


# Q 2: write a Program to display the Fibonacci sequence up to n-th term where n is provided by
# the user

# num = int(input("Enter the number: "))

# def fibonacci(n):
#     l1 = []
#     i =0
#     if n ==0:
#         return "0"
#     while i < n :
#         if(len(l1) == 0):
#             l1.append(i)
#         elif(len(l1) == 1):
#             l1.append(i+ l1[-1])
#         else:
#              l1.append(l1[-1]+ l1[-2])

#         i +=1

#     return ",".join(map(str, l1))

# print("Fibonacci series:", fibonacci(num))

    



# Q 3: Write a Python Program To Display Powers of 2 Using Anonymous Function
# ( Lambda function). Take number of terms from user

# n = int(input("Enter the number of terms: "))

# print("Powers of 2s are: ", list(map(lambda x : 2**x, range(n))) )



# Q 4: Write a Python Program to find numbers divisible by thirteen from a list using anonymous
# function

# l1 = [1,34,657,8,39, 130, 169,546,867743]

# print("List is: ",l1)
# print("Numbers divisible by 13 are: ", list(filter(lambda x : x%13==0, (l1))) )

# Q5: Write a Python program to display the Fibonacci sequence up to n-th term by using recursive
# functions

num = int(input("Enter a number: "))
i =0
l1 = []
def fibonacci(n):
    
    
    if n ==0:
        return "0"

    if(len(l1) == 0):
            l1.append(i)
    elif(len(l1) == 1):
        l1.append(i+ l1[-1])
    else:
         l1.append(l1[-1]+ l1[-2])
        

    if i > n:
        print( ",".join(map(str, l1)) )
        return
    else:
         fibonacci(i+1)

   
fibonacci(num)
    



# Q 6: Write a Python program to find the sum of natural numbers up to n using recursive function

# Q. 7. Write a version of a palindrome recognizer that also accepts phrase palindromes such as
# &quot;Go hang a salami I&#39;m a lasagna hog.&quot;, &quot;Was it a rat I saw?&quot;, &quot;Step on no pets&quot;, &quot;Sit on a potato
# pan, Otis&quot;, &quot;Lisa Bonet ate no basil&quot;, &quot;Satan, oscillate my metallic sonatas&quot;, &quot;I roamed under it as
# a tired nude Maori&quot;, &quot;Rise to vote sir&quot;, or the exclamation &quot;Dammit, I&#39;m mad!&quot;. Note that
# punctuation, capitalization, and spacing are usually ignored.

# Q. 8. A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function
# to check a sentence to see if it is a pangram or not.
# Q.9. Define a function overlapping() that takes two lists and returns True if they have at least one
# member in common, False otherwise.
# Q. 10. Write a function find_longest_word() that takes a list of words and returns the length of
# the longest one.
# Q. 11. Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.


# data = {"2":"two", "3": "three","4":"four" ,"5": "Five" ,"6":"six","7":"Seven" ,"8":"Eight" ,"9":"Nine"}
# print(data.keys())
# print(data.values())
# print(data.items())
# print(len(data))
# if "7" in data:
#     print("7 is present")
# if "2" in data:
#     print("2 is present")    

# print(data["9"])    
# del data["9"]  
# if "9" in data:
#     print("9 is present")    
# else:
#     print("9 is not present")
