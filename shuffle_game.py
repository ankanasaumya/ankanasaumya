from random import shuffle

# Shuffle Game: Three Cup Monte Game

def player_guess():
    
    guess_location = ''
    while guess_location not in ['0','1','2']:
        guess_location = input("Pick a number 0,1 or 2 :")
        #print (guess_location)
    return int(guess_location)


def shuffle_list():
    shuffle(my_list)
    return(my_list)


def guess_value(my_list, guess_location):
    if my_list[guess_location]=='O':
         print('You Win')
    else:
        print('Better Luck Next Time!!')


my_list = ['','O','']
# val= [i for i in my_list if '' != i][0]
mixed_list = shuffle_list()
guess_loc = player_guess()
guess_value(mixed_list, guess_loc)




# guess_value = player_guess()

# if shuffle_list.index('O') == guess_value:
#     print('You Win')
# else:
#     print('Better Luck Next Time!!')
