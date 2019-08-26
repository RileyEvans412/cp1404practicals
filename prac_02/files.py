

user_name = input("Please enter your name ")
file_open = open("name.txt", 'w')
print("Your name is " + user_name, file=file_open)

file_numbers = open("numbers.txt", 'w')
print("17\n42", file=file_numbers)
file_numbers.write("17\n42")
file_numbers.close()

file_numbers = open("numbers.txt", 'r')
number_01 = int(file_numbers.readline())
number_02 = int(file_numbers.readline())
print(number_01 + number_02)
file_numbers.close()

file_numbers = open("numbers.txt", 'w')
for i in range(5):
    file_numbers.write(input("Please enter some numbers: "))

number_list = [" "]
file_numbers = open("numbers.txt", 'r')
for number in file_numbers:
    add_to_list = file_numbers.readline()
    number_list.append(add_to_list)
print(number_list)
