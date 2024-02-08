# ''' code to add odd numbers between 10 to 20 inclusive and store it in x'''

# x = 0

# for i in range(11,21,2):
#     x = x + i
#     print(x)
    
# print(x)




# number = int(input("How many times do i have to tell you?"))
# for i in range(number):
#     print("Clean your room")

''' For every number between 1-20, 20 inclusive, print if 4 and 13 it is unlucky, for ven number print x is even, else print x is odd'''

for x in range(21):
    if x ==4 or x ==13 :
        print(f"{x} is unlucky")
    elif x%2 ==0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")