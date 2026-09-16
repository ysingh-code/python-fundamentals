# 1.if statements
age=20
if age>=18:
    print("you are a valid voter")

# 2.if-elif-else

marks=78
if marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=60:
    print("grade C")
else:
    print("grade D")

# 3.multiple conditions using and

age=20
has_id=True

if age>=18 and has_id:
    print("you are allowed")

# 4.multiple conditions using or

day="Sunday"

if day=="Saturday" or day=="Sunday":
    print("it is a weekend.you can enjoy")

# 5.nested if
age=20
has_id=True
if age>=18:
    if has_id:
        print("entry allowed")
    else:
        print("ID required")
else:
    print("entry not allowed")

# 6.ternary/conditional expression
age=20
result="adult" if age>=18 else "minor"
print(result)