from utils import find_max

input_list = input('Enter number list seperated by ,comma')
list = input_list.split(",")
max = find_max(list)
print(max)