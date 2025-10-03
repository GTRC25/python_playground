# -------------------------
# Football Exception Handling Examples
# -------------------------

# Basic Exception Handling
try:
    goals_per_game = 10 / 0  # Division by zero
    print(goals_per_game)
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Handling Multiple Exception
try:
    player_number = int("ABC")  # ValueError
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

# Catching Multiple Exceptions with Different Blocks
try:
    player_number = int("XYZ")  # ValueError
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# Using Else Block
try:
    goals = 5 / 1  # No Error
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Goals per match: {goals}")

# Using Finally Block
try:
    goals = 8 / 2  # No Error
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print(f"Final Goals: {goals}")

# Raising Exception
try:
    raise ValueError("Invalid football stats")
except ValueError as e:
    print(f"Error: {e}")

# Custom Exception
class LowScoreError(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise LowScoreError("Team score is too low for playoffs")
except LowScoreError as e:
    print(f"Error: {e}")

# Catching All Exceptions
try:
    score = "ten" + 5  # TypeError
except Exception as e:
    print(f"Error: {e}")

# Assertions (Debugging Tool)
total_goals = 12
try:
    assert total_goals >= 0, "Total goals cannot be negative"
    print("Assertion Passed")
except AssertionError as e:
    print(f"Error: {e}")

# Handling Specific Error Type
def divide_goals(goals, matches):
    try:
        avg = goals / matches
    except ZeroDivisionError:
        print("Cannot divide by zero matches")
        return None
    except TypeError:
        print("Invalid input type for goals or matches")
        return None
    else:
        return avg

print(divide_goals(20, 0))
print(divide_goals(15, "five"))
print(divide_goals(18, 3))

# Handling Exception Hierarchy
class FootballError(Exception):
    pass

class PlayerError(FootballError):
    pass

try:
    raise PlayerError("Player not eligible")
except FootballError as e:
    print(f"FootballError: {e}")
except PlayerError as e:
    print(f"PlayerError: {e}")

# Handling Exceptions in List Comprehensions
matches = [2, 0, 4, 5]
results = []
for m in matches:
    try:
        results.append(10 / m)
    except ZeroDivisionError:
        results.append(None)
print(f"Goals per match: {results}")

# Nested Exception Handling
try:
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Inner Error: {e}")
        raise
except Exception as e:
    print(f"Outer Error: {e}")

# Exception Handling with user input
try:
    goals_input = int(input("Enter number of goals scored: "))
    avg = 100 / goals_input
    print(f"Average: {avg}")
except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Context Manager and Exception Handling
class FootballMatch:
    def __enter__(self):
        print("Starting match...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Ending match...")
        if exc_type:
            print(f"Error during match: {exc_value}")
        return True  # Suppress exception

with FootballMatch() as match:
    print("Playing match...")
    raise ValueError("Simulated match error")

# Exception Propagation
def match_a():
    raise ValueError("Error in match_a stats")

def match_b():
    try:
        match_a()
    except ValueError as e:
        print(f"Handled in match_b: {e}")
        raise  # Propagate

try:
    match_b()
except ValueError as e:
    print(f"Handled in main: {e}")
