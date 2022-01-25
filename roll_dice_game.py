import random


class Dice:
    def roll(self):
        x1=random.randint(1,6)
        x2=random.randint(1,6)
        return x1,x2 #for tuples paranthesis not required


number1 = Dice()
print(number1.roll())
# number2 = Dice()
# output2 = number2.roll()
# print(f'({output1})')
# print(f'({output1},{output2})')

