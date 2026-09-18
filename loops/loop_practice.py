#LOOP PRACTICE

# Q1. accept an integer and print 'hello world' n times
n=int(input("enter how many times you want to print hello world"))
for i in range(n):
    print("hello world")

# Q2.print natural numbers from 1 to n
n=int(input("enter a number"))
for i in range(1,n+1):
    print(i)

# Q.3 reverse for loop.print n to 1
n=int(input("enter a number"))
for i in range(n,0,-1):
    print(i)

# Q4.take a number as input and print its multiplication table
n=int(input("enter a number"))
print(f"multiplication table of {n} is:-")
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

# Q5. find the sum of numbers up to n
n=int(input("enter a number"))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"sum of numbers from 1 to {n} is {sum}")

# Q6.find the factorial of a number
n=int(input("enter a number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(f"factorial of {n} is {fact}")

# Q7.print the sum of all even and odd numbers in a range separately
n=int(input("enter the range:-"))
even_sum=0
odd_sum=0
for i in range(1,n+1):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print(f"the even sum and odd sum from this {n} range is {even_sum} and {odd_sum} respectively")

# Q8.print all the factors of a number
n=int(input("enter a number:-"))
for i in range(1,n+1):
    if n%i==0:
        print(i)

# Q9. accept a number and check it is a perfect number or not
n=int(input("enter a number:-"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if n==sum:
    print("it is perfect")
else:
    print("it is not perfect")

# Q10. check whether the number is prime or not
n=int(input("enter a number:-"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("it is prime")
else:
    print("it is not prime")

# Q11.reverse a string without using builtin functions
name="yuvraj singh"
for i in range(len(name)-1,-1,-1):
    print(name[i],end="")

# Q12.check whether a string is palimdrome or not
name="naman"
rev=""
for i in range(len(name)-1,-1,-1):
    rev=rev+name[i]

if rev==name:
    print("it is palindrome")
else:
    print("it is not palindrome")

# Q13. count all letters,digits,and special symbols from a given string
str="dfef4446sfffffkfgl5f6f8*&%#$@856"
letters=0
digits=0
spcchar=0
for i in range(0,len(str),1):
    if str[i].isalpha():
        letters+=1
    elif str[i].isdigit():
        digits+=1
    else:
        spcchar+=1
print(f"total number of letter is {letters} and digits is {digits} and special character is {spcchar}")