#functions practice

# 1. simple function

def greet():
    print("hello world")

greet()

# 2.function with one parameter

def greet_user(name):
    print(f"hello {name}")

greet_user("yuvraj")
greet_user("virat")


# 3.function with multiple parameter

def add(a,b):
    print(f"sum:{a+b}")

add(12,45)
add(200,455)

# 4. Positional argument

def student(name,age):
    print(f"name:{name}")
    print(f"age:{age}")
student("yuvraj",22)

# 5. Default argument

def welcome(name="student"):
    print(f"WELCOME {name}")
welcome("rahul")
welcome()

# 6. Keyword argument

def introduce(name,age,city):
    print(f"name:{name}")
    print(f"age:{age}")
    print(f"city:{city}")

introduce(age=22,city="bhubaneswar",name="yuvraj singh")