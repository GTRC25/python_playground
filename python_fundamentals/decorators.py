"""Write a Python decorator called repeat_twice that makes any function run two times automatically.
Then, create a function cheer(team) that returns "Go {team}!".
Apply your @repeat_twice decorator to cheer.
Finally, call cheer("Barcelona") and print the result.
"""
from itertools import count


# Step 1: Create the decorator
def repeat_twice(func):
    def wrapper(*args, **kwargs):
        # Call the original function two times
        result1 = func(*args, **kwargs)
        result2 = func(*args, **kwargs)
        return result1 + "\n" + result2  # Join results with a newline
    return wrapper

# Step 2: Create a function and apply the decorator
@repeat_twice
def cheer(team):
    return f"Go {team}!"

# Step 3: Call the decorated function
print(cheer("Barcelona"))


"""Create a decorator called goal_celebration that adds “⚽ Goal!” at the end of whatever the function returns.
Then, write a function score(player) that returns "Player {player} scored".
Apply your @goal_celebration decorator to the score function.
Call score("Messi") and print the result."""

def goal_celebration(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@goal_celebration
def score(player):
    return f"player {player} scored"

print(score("Messi"))


"""Create a decorator called announce_goals that will count how many players scored in a match.
Every time the decorated function is called, it should print:
"Goal {count} scored!" before returning the original message.
The decorator should remember the count across multiple function calls.
Write a function score(player) that returns "Player {player} scored".
Apply the @announce_goals decorator to score.
"""

def announce_goals(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        print(f"goal {count} scored")
        result = func(*args, **kwargs)
        return result
    return wrapper

@announce_goals
def score(player):
    return f"player {player} scored at 26th minute"

print(score("Ferran torres"))



# Class-based decorator
class GoalDecorator:
    def __init__(self, func):
        self.func = func      # Store the original function
        self.count = 0        # Track how many times the function is called

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Goal {self.count} scored!")  # Extra behavior
        return self.func(*args, **kwargs)    # Call the original function

# Function to decorate
@GoalDecorator
def score(player):
    return f"Player {player} scored."

# Test calls
print(score("Messi"))
print(score("Ronaldo"))






