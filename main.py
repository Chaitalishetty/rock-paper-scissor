import random

values = ['paper', 'rock', 'scissor']


def user_value():
    i = 3
    while i > 0:
        comp_value = random.choice(values)
        
        option = input("enter\n")
        print(comp_value)
        if option == comp_value:
            print("draw")
        elif option == 'rock':
            if comp_value == 'scissor':
                print("You win")
            elif comp_value == 'paper':
                print("You lose")
                i -= 1
        elif option == 'scissor':
            if comp_value == 'paper':
                print("You win")
            elif comp_value == 'rock':
                print("You lose")
                i -= 1
        elif option == 'paper':
            if comp_value == 'rock':
                print("You win")
            elif comp_value == 'scissor':
                print("You lose")
                i -= 1
        print(i)


user_value()

