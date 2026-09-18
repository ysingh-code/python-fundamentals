#for loop practice

# 1.print numbers from 1 to 10
for i in range(1,11):
    print(i)

# 2.print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)
# 3. print even numbers from 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i)

# 4.print odd numbers from 1 to 20
for i in range(1,21):
    if i%2!=0:
        print(i)

# 5. multiplication table
n=int(input("enter anumber:-"))

for i in range(1,11):
    print(f"{n}*{i}={n*i}")

# 6.iterate through a string character by character

name="Yuvraj"
for i in name:
    print(i)

# 7.iterate through a string using index values

name="yuvraj singh"
for i in range(len(name)):
    print(name[i])

# 8.count characters using a for loop
name="parshuram"
count=0
for i in name:
    count+=1
print("number of characters",count)

# 9.find sum from 1 to n
n=int(input("enter n:-"))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"your sum of 1 to {n} is {sum}")

# 10.print natural numbers from 1 to n
n=int(input("enter n:-"))
for i in range(1,n+1):
    print(i)   