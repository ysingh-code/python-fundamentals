# 1. Break
'''
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# 2. Continue

for i in range(1, 11):
    if i == 6:
        continue

    print(i)

# 3. Loop Else

for i in range(1, 6):
    print(i)
else:
    print("Loop completed successfully")'''

# 4. Loop Else with Break

for i in range(1, 11):
    if i == 6:
        break

    print(i)
else:
    print("Loop completed successfully")
