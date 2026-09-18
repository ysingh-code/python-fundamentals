# 1.print numbers from 1 to 10
i=1
while i<=10:
    print(i)
    i+=1


# 2.print numbers from 20 to 1
i=20
while i>0:
    print(i)
    i-=1

# 3.print natural numbers up to n
number=int(input("enter n:-"))
i=1
while i<=number:
    print(i)
    i+=1

# 4.separate each digit of a number
num=int(input("give me a multi digit number:-"))
while num!=0:
   digit= num%10
   print(digit)
   num=num//10



# 5. reverse a number
num=int(input("give me a multi digit number:-"))
rev=0
while num!=0:
   digit= num%10
   rev=rev*10+digit
   num=num//10
print(f"reverse of this number is {rev}")

# 5. check whether the number is palindrome
num=int(input("give me a multi digit number:-"))
rev=0
org=num
while num!=0:
   digit= num%10
   rev=rev*10+digit
   num=num//10

if org==rev:
   print("it is a palindrome")
else:
   print("this is not a palindrome")