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
import units
import volume
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
        x = input("Please select what you'd like to calculate... \n[1] SA and Volume \n[2] Rockets \n[3] Fuel Consumption \n[4] Gravity of Object \n[5] Velocity of Rotate (Takeoff) \n[6] Fuel Requirement \n[7] Convert Units \n[8] Play Roulette \n[9] Play Keep-Under-10 \n[10] Play Guess the Word \n> ").strip()
        if x == "1":
            volume.rad()
        elif x == "2":
            rockets.rockets()
        elif x == "3":
            燃油消耗.fuel()
        elif x == "4":
            牛逼1.nb1()
        elif x == "5":
            起飞速度.VR()
        elif x == "6":
            one.calc()
        elif x == "7":
            units.unit()
        elif x == "8":
            roulette.roulette()
        elif x == "9":
            mathgame.game()
        elif x == "10":
            game.chooseword()
        else:
            print("Invalid input, please try again")
        pass
    
    
    
    
if __name__ == "__main__":
    main()