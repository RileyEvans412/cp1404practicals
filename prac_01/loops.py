for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
First Question
"""
for i in range(0, 101, 10):
    print(i, end=' ')


"""
Second Question
"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""
Third Question
"""
user_stars = int(input("\n How many stars would you like to print?: "))
print("*" * user_stars)


"""
Third Question
"""
for i in range(1, user_stars + 1):
    print("*" * i)