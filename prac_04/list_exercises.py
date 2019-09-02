list_of_numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

for number in range(5):
    user_numbers = int(input("Please enter a number: "))
    list_of_numbers.append(user_numbers)
print("Numbers:", list_of_numbers)
print("The first number is {}".format(list_of_numbers[0]))
print("The last number is {}".format(list_of_numbers[-1]))
print("The smallest number is {}".format(min(list_of_numbers)))
print("The largest number is {}".format(max(list_of_numbers)))
print("The average of all numbers is {}".format(sum(list_of_numbers) // len(list_of_numbers)))

user_name = input("Please enter a correct username: ")
if user_name not in usernames:
    print("Access Denied")
else:
    print("Access Granted")