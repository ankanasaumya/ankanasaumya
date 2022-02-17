'''

Addition of Numbers
Number1= input("Enter Number 1: ")
Number2= input("Enter Number 2: ")
Total= float(Number1) + int(Number2)
print(Total)

def addTwoNumbers(a,b, args, kargs*):

#f, u and r string

course = 'python for developers'
print(course.upper())
print(course.find('p'))


#Excercise: Weight Conversion

Weight = float(input(' Enter your Weight: '))
kg_lbs= input('(K)gs or (L)bs: ').lower()
if(kg_lbs == 'k'):
   # print('Weight in Kg: '+ str(Weight))
    Weight = Weight * 2.204
    print(f"Weight in lbs: {Weight}")
elif(kg_lbs == 'l'):
    Weight = Weight / 2.204
    print(f"Weight in lbs: {Weight}")
else:
    print ('Not a valid input')


#Guess Game!!!
sec_num = 7
i=0
while(i<3):
    i+=1
    guess = int(input('Guess :'))
    if(guess == sec_num):
        print('You Win!!')
        break
else:
        print('you failed!!')    


# Car Game
print('welcome to Car Game')
print("""select the input from the list 
\n help
\n start
\n stop
\n quit""")
command = ""
x=0 
y=0
while True:
    command = input("> ").lower()
    if(command == 'help'):
        print(""" 
Start - to start the car
Stop - to stop the car
quit - to exit
""")
    elif(command == 'start' and x==0):
        print('Car Started... Ready To Go')
        x+=1
        y=0
    elif(command == 'start' and x==1):
            print('Car already started!!')
    elif(command == 'stop' and y==0):
        print('Car Stopped')
        y+=1
        x-=1
    elif(command == 'stop' and y==1):
        print('Dude!! What you doin? Car is already Stopped')
    elif (command =='quit'):
        break
    else:
        print('invalid input')

print('welcome to Car Game')
print("""select the input from the list 
\n help
\n start
\n stop
\n quit""")
command = ""
started = False
while True:
    command = input("> ").lower()
    if(command == 'help'):
        print(""" 
Start - to start the car
Stop - to stop the car
quit - to exit
""")
    elif(command == 'start'):
        if started:
            print('Car already started!!')
        else:
            started = True
            print('Car Started... Ready To Go')
    elif(command == 'stop'):
        if not started:
            print('Dude!! What you doin? Car is already Stopped')
        else:
            started = False
            print('Car stopped!!')
    elif (command =='quit'):
        break
    else:
        print('invalid input')

print('welcome to Car Game')
print("""select the input from the list 
\n help
\n start
\n stop
\n quit""")
i = 0
while i<100:
    command = input("> ").lower()
    if(command == 'help'):
        print(""" Start - to start the car
            Stop - to stop the car
            quit - to exit""")
    elif(command == 'start'):
        print('Car Started... Ready To Go')
    elif(command == 'stop'):
        print('Car Stopped')
    elif (command =='quit'):
        break
    else:
        print('invalid input')
    i+=1'''

# numbers = [5,2,5,2,2]
# for x in range(5):
#     print('')
#     for num in numbers:
#         print('x', end='')

# numbers = [5,2,5,2,2]
# for num in numbers:
#     # print(num)
#     print('')
#     for i in range(num):
#         print('x', end='')

# x=0
# y=0
# names = ['a','b','c']
# length = len(names)
# # print(length)
# store = names[y]
# for name in names:
#     for x in range(1):
#         print(f'({name},{store})')
#         y+= 1

# x=0
# y=0
# names = ['a','b','c']
# length = len(names)
# print(length)
# for name in names:
#     for x in range(length):
#         for y in range(length-1):
#             print(f'{names[x]},{names[y]}')
            
            # print(f'{name},{names[length-1]}')
            # length-=1
#print(names[1:2])
# for name in names:
#     #print(name)
#     for x in range(name):
    #     print(f'({names},{names})')

#Max in List

# x,y,i = 0,0,0
# list = ['1','2','6','4','5']
# length = len(list)
# for max in list:
#     for x in range(length+1):
#         if(x>x):
#             y = x
#         else:
#             x+= 1
# print(y)

x = 7 % 4
y = 2 ** 3
print(x,y)

