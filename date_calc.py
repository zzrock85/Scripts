from datetime import datetime
from dateutil.relativedelta import relativedelta

# Set the default date to today in YYYY-MM-DD format
default_date = datetime.today().strftime('%Y-%m-%d')

def show_menu():
    """
    Display the main menu and handle user selection.
    """
    while True:
        print("\n--- Date calculation ---")
        print("1. Difference between dates")
        print("2. Add or subtract days")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            diff_date()
        elif choice == "2":
            add_subtract_menu()
        elif choice == "3":
            print("See you!")
            break
        else:
            print("Invalid selection. Please try again.")

def diff_date():
    """
    Calculate and display the difference between two dates.
    """
    first_date = input(f"Enter the first date in the format YYYY-MM-DD [{default_date}]:") or default_date
    second_date = input("Enter the second date in the format YYYY-MM-DD: ")
    try:
        start_date = datetime.strptime(first_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(second_date, "%Y-%m-%d").date()
        print(f"\nFirst date is: {start_date}")
        print(f"Second date is: {end_date}")
    except ValueError:
        print("Incorrect date format! Use YYYY-MM-DD.")
    # Calculating the difference
    if start_date < end_date:
        delta = relativedelta(end_date, start_date)
        total_days = (end_date - start_date).days
    else:
        delta = relativedelta(start_date, end_date)
        total_days = (start_date - end_date).days
    # Displaying results
    print(f"\nYears: {delta.years}")
    print(f"Months: {delta.months}")
    print(f"Weeks: {delta.weeks}")
    days = delta.days - delta.weeks*7
    print(f"Days: {days}")
    # Calculating weeks and days
    weeks = total_days // 7
    if days == 1:
        print(f"\nTotal number of weeks: {weeks:,} and {days} day")
    else:
        print(f"\nTotal number of weeks: {weeks:,} and {days} days")
    print(f"Total number of days: {total_days:,}")

def add_subtract_menu():
    """
    Menu for adding or subtracting years, months, and days from a date.
    """
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Back to main menu")

        choice = input("Select an option: ")

        if choice in ("1", "2"):
            date_add_subtract(choice)
        elif choice == "3":
            return
        else:
            print("Invalid selection. Please try again.")

def date_add_subtract(choice):
    """
    Add or subtract years, months, and days from a given date.
    """
    first_date = input(f"Enter the date in the format YYYY-MM-DD [{default_date}]:") or default_date
    start_date = datetime.strptime(first_date, "%Y-%m-%d").date()
    print("Please enter what you want to add or subtracr")
    lata_input = input("How many years? [0]: ") or "0"
    miesiace_input = input("How many months? [0]: ") or "0"
    days_input = input("How many days? [0]: ") or "0"
    lata = int(lata_input)
    miesiace = int(miesiace_input)
    days = int(days_input)
    if choice == "1":
        new_date = start_date + relativedelta(years=lata, months=miesiace, days=days)
    elif choice == "2":
        new_date = start_date - relativedelta(years=lata, months=miesiace, days=days)
    print(f"\nOld date: {start_date}")
    print(f"New date: {new_date}\n")

# Start the program by showing the menu
show_menu()
