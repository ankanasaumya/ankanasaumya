#Find Out Maxmium Value in the List
numbers = [5,3,15,2,10] #list if specified in '' will be treated as string
max = numbers[0]
for number in numbers: #Loop for 
    if number > max:
        max = number
print(max)