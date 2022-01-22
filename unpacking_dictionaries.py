# unpacking : The way of assignment to variables

# coordinates = (1,2,3)
# # x= coordinates[0] to avoid repetation of task "unpacking" can be used
# # y= coordinates[1]
# # z= coordinates[2]

# x, y, z = coordinates
# print(x,y,z)

#Dictionaries
# customer = {
#     "name": "Ankana S",
#     "age" : 32,
#     "is Verified": True
# }
# print(customer["name"])

#Exercise
# Take Input of Phone number and print it in words
'''
phone = input("enter phone no")
digits = {
    "1": "one", #defining dictionaries for mapping the digits
    "2": "Two"
}
#to search the character in the string
output = ""
for ch in phone:
    output+=digits.get(ch, "!") + " " #get function is used to retrive the value from dictionaries
print(output)
'''

# Excercise2
# Emoji converter
message = input(">")
words = message.split(" ")
smiley = {          #dictionaries
    ":)" :"😀",
    ":(" :"😒"
}
output  =""
for word in words:
    output += smiley.get(word, word) + " "
print(output)