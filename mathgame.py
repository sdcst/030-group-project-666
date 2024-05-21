import random

def add_subtract_multiply_divide_game():
    total = 5
    print("Welcome to the Add/Subtract/Multiply/Divide Game! \n Try to keep the total between 0 and 10.")

    for i in range(10000000000000000000000):
        print(f"\nCurrent total: {total}")
        number = random.randint(1, 5)
        print(f"The random number is: {number}")
        choice = input("Would you like to (1. multiply) (2. divide) (3. subtraction) (4. addition) > ").strip()
        
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please enter 1 to multiply, 2 to divide, 3 to subtract, or 4 to add.")
            continue

        if choice == "1":
            total = total * number
            print(f"You multiplied by {number}. New total: {total}")
        elif choice == "2":
            if number != 0:
                total /= number
                print(f"You divided by {number}. New total: {total}")
            else:
                print("Division by zero is not allowed. Choose a different operation.")
        elif choice == "3":
            total = total - number
            print(f"You subtracted by {number}. New total: {total}")
        elif choice == "4":
            total = total + number
            print(f"You added by {number}. New total: {total}")
            continue
        
        if total < 0 or total > 10:
            print("\nTotal is out of the range 0-10. You lose!")
            break
        
        play_again = input("Would you like to continue? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    add_subtract_multiply_divide_game()