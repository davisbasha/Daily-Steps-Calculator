# Define global variables to hold the user's daily goal and the total number of steps taken in a week.
daily_goal = 0
total_steps = 0

def main():
    # The main function orchestrates the flow of the program by calling other functions in sequence.
    set_steps_goal()  # Sets the user's daily steps goal.
    record_daily_steps()  # Records the number of steps taken each day for a week.
    evaluate()  # Evaluates and prints the user's performance against their goal.

def set_steps_goal():
    # This function prompts the user to set their daily steps goal.
    global daily_goal  # Specifies that the function will use the global 'daily_goal' variable.
    daily_goal = int(input("Enter your daily steps goal: "))  # Asks the user to input their goal and stores it.

def record_daily_steps():
    # This function records the number of steps taken by the user each day for a week.
    global total_steps  # Specifies that the function will use the global 'total_steps' variable.
    day_count = 0  # Initializes a counter to keep track of the days.
    while day_count < 7:  # Loops until steps for all 7 days are recorded.
        steps = int(input(f"Enter steps for day {day_count + 1}: "))  # Asks the user to input their steps for the day.
        total_steps += steps  # Adds the steps for the day to the total steps count.
        day_count += 1  # Increments the day counter.

def evaluate():
    # This function evaluates the user's weekly performance against their daily goal.
    print(f"Your daily steps goal is {daily_goal:,}.")  # Prints the user's daily goal.
    average_steps = total_steps / 7  # Calculates the average number of steps taken per day over the week.
    print(f"Your average daily steps: {average_steps:,.0f}")  # Prints the average daily steps.
    # Compares the average daily steps against the daily goal and prints the user's performance outcome.
    if average_steps > daily_goal:
        print("You did better than your daily goals this week.")  # User exceeded their goal.
    elif average_steps < daily_goal:
        print("You could not achieve your daily goal this week.")  # User did not meet their goal.
    else:
        print("You met your goal this week.")  # User exactly met their goal.

main()