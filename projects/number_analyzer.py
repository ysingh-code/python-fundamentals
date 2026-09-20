"""
Number Analyzer

A mini Python project that takes a number as input and analyzes
its different properties, including whether it is positive or negative,
even or odd, its digit count, digit sum, reverse, palindrome status,
prime status, factors, and whether it is a perfect number.

"""
number=int(input("Give a number to analyzes:-"))
temp=abs(number) #taking absolute value fron analyse negative number
temp2=abs(number)
#positive/negative/0 test
if number>0:
    res="positive"
elif number<0:
    res="negative"
else:
    res="Zero"

#even/odd test
if number%2==0:
    eo_test="even"
else:
    eo_test="odd"

#number of digits of the given number
count=0
digit_sum=0
rev=0
while temp>0:
    digit=temp%10
    count+=1
    digit_sum=digit_sum+digit #sum of digits
    rev=rev*10+digit #reverse the number
    temp=temp//10
# check the number is palindrome or not
if number<0:
    palindrome="no"
elif rev==number:
    palindrome="yes"
else:
    palindrome="no"
# check the number is prime or not
if number>1:
    g=0

    for i in range(1,number+1):
            if number%i==0:
             g+=1
    if g==2:
        prime="yes"
    else:
        prime="no"
else:
    prime="no"
    

# find all factors of the number

factors=[]

for i in range(1,temp2+1):
    if temp2%i==0:
        factors.append(i)

#check the number is perfect number or not
perfect=""
total=0
for i in range(1,number):
    if number%i==0:
        total+=i
if total==number and number>0:
    perfect="yes"
else:
    perfect="no"


print(f"Number:{number}")
print(f"Type:{res}")
print(f"Even/Odd:{eo_test}")
if number==0:
    print(f"Number of digits:1")
else:
    print(f"Number of digits:{count}")
print(f"Sum of digits:{digit_sum}")
if number<0:
    print(f"Reverse of digits of this number is:{rev}")
else:
    print(f"Reverse:{rev}")
print(f"Palindrome:{palindrome}")
print(f"Prime:{prime}")
if number>0:
    print(f"Factors:{factors}")
elif number==0:
    print(f"Factors:infinite or indefinite")
else:
    print(f"Positive Factors:+{factors}")
    print(f"Negative factors:-{factors}")
print(f"Perfect number:{perfect}")
        




         







