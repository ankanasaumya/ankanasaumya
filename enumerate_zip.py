mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1,mylist2): #zip function merge the two and list together
    print(item) #it will print tuples with 2 items

#In uneven list length, zip function will merge the list till the length of shortest list.