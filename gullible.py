"""Gullible, by Al Sweigart al@inventwithpython.com
How to keep a gullible person busy for hours. (This is a joke program.)
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, humor"""

print('Gullible, by Cephas Mutua')
counter = 1
a = "really"
while True: # Main program loop.
    print('Do you ',a*counter, 'want to know how to keep gullible person busy for hours? Y/N')
    response = input('> ') # Get the user's response.
    if response.lower().startswith('n'):
        break # If "no", break out of this loop.
    if response.lower().startswith('y'):
        counter+=1
        continue # If "yes", continue to the start of this loop.
    print('"{}" is not a valid yes/no response.'.format(response))

print('Thank you. Have a nice day!')