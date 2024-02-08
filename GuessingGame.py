import random
rand_num = random.randint(1,10)

human = ''

while human != rand_num:
    human = int(input("Enter your number choice\n"))
    if human < rand_num:
        print("Too Low!!!")
    elif human > rand_num:
        print("Too High!!!")
    else:
        print("You are correct!!!")
        play_again = input("do you want to play again? y/n\n").lower()
        if play_again == 'y':
            rand_num = random.randint(1,10)
            human = ''
        else:
            break
            
    

