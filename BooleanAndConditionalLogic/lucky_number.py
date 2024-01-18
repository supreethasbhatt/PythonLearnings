from random import randint

choice = randint(1,10)

if choice == 7:
    print("lucky")
else:
    print("unluky")
    
    
''' to check if a number is even or odd'''

number = randint(1,10)

if number%2 == 0:
    print("even")
else:
    print("odd")
    
''' input from user '''
number = input("Enter a number\n")
number = int(number)

if number%2 == 0:
    print("even")
else:
    print("odd")