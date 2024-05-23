#!python3
# Volume Calculator
# Feel free to rename your variables
import rockets
import roulette
import 燃油消耗
import 牛逼1
import mathgame
import one
import game
import 起飞速度
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
        x = input("Please select what you'd like to calculate... \n[1] Rockets \n[2] Fuel Consumption \n[3] Gravity of Object \n[4] Velocity of Rotate (Takeoff) \n[5] Fuel Requirement \n[6] Play Roulette \n[7] Play Keep-Under-10 \n[8] Play Guess the Word \n> ").strip()
        if x == "1":
            rockets.rockets()
        elif x == "2":
            燃油消耗.fuel()
        elif x == "3":
            牛逼1.nb1()
        elif x == "4":
            起飞速度.VR()
        elif x == "5":
            one.calc()
        elif x == "6":
            roulette.roulette()
        elif x == "7":
            mathgame.game()
        elif x == "8":
            game.chooseword()
        else:
            print("Invalid input, please try again")
        pass
    
    
    
    
if __name__ == "__main__":
    main()