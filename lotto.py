import random


def show_menu():
    while True:
        print("Lotto Number Generator")
        print("1. Generate Lotto Numbers")
        print("2. Generate Mini Lotto Numbers")
        print("3. Generate Eurojackpot Numbers")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            generate_lotto_numbers()
        elif choice == "2":
            generate_mini_lotto_numbers()
        elif choice == "3":
            generate_eurojackpot_numbers()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid selection. Please try again.\n")

def generate_lotto_numbers():
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()
    print ("Lotto, 1-49, 6 numbers")
    print("Numbers drawn:", numbers, "\n")

def generate_mini_lotto_numbers():
    numbers = random.sample(range(1, 43), 5)
    numbers.sort()
    print ("Mini Lotto, 1-42, 5 numbers")
    print("Numbers drawn:", numbers, "\n")

def generate_eurojackpot_numbers():
    numbers = random.sample(range(1, 51), 5)
    numbers.sort()
    numbers_2 = random.sample(range(1, 13), 2)
    numbers_2.sort()
    print ("Eurojackpot, 1-50, 5 numbers")
    print("Numbers drawn:", numbers)
    print ("Eurojackpot, 1-12, 2 numbers")
    print("Numbers drawn:", numbers_2, "\n")

# Start the program by showing the menu
show_menu()