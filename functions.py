# defining functions

# def greet_by_name(): #define function by def
#     print('Hi there!!')
#     print ('How are you?')

# print("start")
# greet_by_name()
# print('completed')

#Parameters
#parameters and arguments
#parameters : function called for receieving the data
#arguments: functions called for supplying the data
def greet_by_name(first_name,last_name): #when function has parameter i.e. here its name then we are obligate to pass value for the parameter
    print(f'Hi {first_name} {last_name}!!')
    print ('How are you?')

print("start")
greet_by_name("Ankana","Saumya") #positional arguments
# calc_cost(total=50,cost=5,discount=0.1) #this is keyword arguments
#however, if using both the positional and keyword argumnet then,
#keyword arguments will always be defined after positional arguments
print('completed')

#return statement
def area(length,breadth):
    return (length * breadth) #if return not specified it will give as none 
print(area(3,4))

def smiley_converter(message):
    words = message.split(" ")
    smiley = {          #dictionaries
        ":)" :"😀",
        ":(" :"😒"
    }
    output  =""
    for word in words:
        output += smiley.get(word, word) + " "
    return output


message = input(">")
print(smiley_converter(message))