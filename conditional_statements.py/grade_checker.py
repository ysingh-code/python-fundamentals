marks=int(input("give your marks"))
if marks>100 or marks<0:
    print("INVALID MARKS!")
elif marks>=90 :
    print("grade A")
elif marks>=75 :
    print("grade B")
elif marks>=60:
    print("grade C")
elif marks>=40:
    print("grade D")
else:
    print("grade F")

