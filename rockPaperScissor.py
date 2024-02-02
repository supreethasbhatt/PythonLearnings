''' This is a program for rock paper scissors.'''
from random import randint



def computerplayer(value):
    if value == 0:
        computer = 'rock'
    elif value == 1:
        computer = 'scissor'
    else:
        computer = 'paper'
    return computer

def play_with_computer(computer_value):
    player1 = input('Player pleae enter your option between rock paper scissors\n')
    if computer_value == 'rock' :
        if player1 == 'scissor':
            win = 'Computer'
            print(f"Computer played {computer_value}, player played {player1}, Computer wins!!")
        elif player1 == 'paper':
            win = 'Player'
            print(f"Computer played {computer_value}, player played {player1}, Player wins!!")
        else:
            win = 'No one'
            print(f"Computer played {computer_value}, player played {player1},  It's a tie!!")
    elif computer_value == 'paper' :
        if player1 == 'scissor':
            win = 'Player'
            print(f"Computer played {computer_value}, player played {player1}, Player wins!!")
        elif player1 == 'rock':
            win = 'Computer'
            print(f"Computer played {computer_value}, player played {player1}, Computer wins!!")
        else:
            win = 'Its a tie!!'
            print(f"Computer played {computer_value}, player played {player1},  It's a tie!!")
    else:
        if player1 == 'paper':
            win = 'Player'
            print(f"Computer played {computer_value}, player played {player1}, Player wins!!")
        elif player1 == 'rock':
            win = 'Computer'
            print(f"Computer played {computer_value}, player played {player1}, Computer wins!!")
        else:
            win = 'No one'
            print(f"Computer played {computer_value}, player played {player1},  It's a tie!!")
    
    

def players_game():
    player1 = input("Player 1, please enter your choice : Rock, Paper, scissor\n")
    player2 = input("Player 2, please enter your choice : Rock, Paper, Scissor\n")
    
    if player1 == 'rock' :
        if player2 == 'scissor':
            win = 'Player1'
            print(f"Player1 played {player1}, player played {player2}, Player1 wins!!")
        elif player2 == 'paper':
            win = 'Player2'
            print(f"Player1 played {player1}, player played {player2}, Player2 wins!!")
        else:
            win = 'No one'
            print(f"Player1 played {player1}, player played {player2},  It's a tie!!")
    elif player1 == 'paper' :
        if player2 == 'scissor':
            win = 'Player2'
            print(f"Player1 played {player1}, player played {player2}, Player2 wins!!")
        elif player2 == 'rock':
            win = 'Player1'
            print(f"Player1 played {player1}, player played {player2}, Player1 wins!!")
        else:
            win = 'No one'
            print(f"Player1 played {player1}, player played {player2},  It's a tie!!")
    else:
        if player2 == 'paper':
            win = 'Player2'
            print(f"Player1 played {player1}, player played {player2}, Player2 wins!!")
        elif player2 == 'rock':
            win = 'player1'
            print(f"Player1 played {player1}, player played {player1}, Player1 wins!!")
        else:
            win = 'No one'
            print(f"Player1 played {player1}, player played {player2},  It's a tie!!")

def start():
    player0 = input("Enter if you want to play with the Computer or Player\n").lower()
    if player0 == 'computer':
        value=randint(0,2)
        computer_value = computerplayer(value)
        win= play_with_computer(computer_value)
        print(f"{win} wins the game")
    elif player0 == 'player':
        win=players_game()
        print(f"{win} wins the game")
    else:
        print("Chose either Computer or Player\n")

if __name__ == '__main__':
    start()
