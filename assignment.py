#!python3
# Volume Calculator
# Feel free to rename your variables
import rockets
import roulette
import 燃油消耗
import 牛逼1
import mathgame
import one

import 牛逼1
def title(a = "*", b = " "):
    print(f"{a * 12} THE CALCULATOR {a*12} \n {b * 12} BY: 芝士666 {b*12}")
    return None

def instructions():
    print("Welcome to THE CALCULATOR, where you'll be able to calculate stuff from various areas, and even play some games revolving around numbers. \n In order to pick stuff, you must enter the number listed next to the option.")
    return None



def main():

    title()
    instructions()
    while True:
        x = input("Please select what you'd like to calculate... \n[1] Rockets \n[2] Fuel Consumption \n[3] Gravity of Object \n[4] Fuel Requirement \n[5] Play Roulette \n[6] Play Keep-Under-10 \n> ").strip()
        if x == "1":
            rockets.rockets()
        elif x == "2":
            燃油消耗.fuel()
        elif x == "3":
            牛逼1.nb1()
        elif x == "4":
            one.calc()
        elif x == "5":
            roulette.roulette()
        elif x == "6":
            mathgame.game()
        else:
            print("Invalid input, please try again")
        pass
    
    
    
    
if __name__ == "__main__":
    main()