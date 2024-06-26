import random
def spin_wheel():
    numbers = list(range(37))
    colors =  ['Green']+(['Red', 'Black'] * 18)
    spin = random.randint(0, 36)
    return numbers[spin], colors[spin]

def roulette():
    print("Welcome to Russian Wheel Roulette!, you have ")
    bet = input("Place your bet (number 0-36 or red/black/Green)> ")
    bet = bet.strip()
    bet = bet.lower()

    if bet.isdigit():
        bet = int(bet)
        if bet < 0 or bet > 36:
            print("Invalid bet. Number must be between 0 and 36, please try again")
            main()
            return
    elif bet in ['red', 'black', 'green']:
        bet = bet.capitalize()
    else:
        print("Invalid bet. Please bet on a number (0-36) or color (Red/Black/Green).")
        main()
        return


    number, color = spin_wheel()
    print(f"The wheel spins... and lands on {number} {color}!")

    if (isinstance(bet, int) and bet == number) or (bet == color):
        
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")
    
    for i in range(10000000000000000000000000000000000):
        x = (input("Would you like to play again? (1. yes)(2. no)> "))
        if x == "1":
            main()
            break
        elif x == "2":
            break
        else:
            print("Your entry is invalid, try again (number only)")

def main():
    roulette()
        
if __name__ == "__main__":
    main()   


