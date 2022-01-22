#remove duplicate numbers

numbers = [1,2,3,4,3,2,8]
check = []
# numbers.sort()
for duplicate in numbers:
    if duplicate not in check:
        check.append(duplicate)
print(check)