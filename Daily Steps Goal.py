# Define global variables to hold the user's daily goal and the total number of steps taken in a week.
daily_goal = 0
total_steps = 0

def main():
    #The main function orchestrates the flow of the program by calling other functions in sequence.
    set_steps_goal()
    record_daily_steps()
    evaluate()

def set_steps_goal():
    #This function prompts the user to set their daily steps goal.
    global daily_goal
    daily_goal = int(input("Enter your daily steps goal: "))
def record_daily_steps():
    #This function records the number of steps taken by the user each day for a week.
    global total_steps
    day_count = 0
    while day_count < 7:
        steps = int(input(f"Enter steps for day {day_count + 1}: "))
        total_steps += steps
        day_count += 1

def evaluate():
    #This function evaluates the user's weekly performance against their daily goal.
    print(f"Your daily steps goal is {daily_goal:,}.")
    average_steps = total_steps / 7
    print(f"Your average daily steps: {average_steps:,.0f}")

    if average_steps > daily_goal:
        print("You did better than your daily goals this week.")
    elif average_steps < daily_goal:
        print("You could not achieve your daily goal this week.")
    else:
        print("You met your goal this week.")

main()