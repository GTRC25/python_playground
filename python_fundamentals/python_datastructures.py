# Lists - Ordered, Mutable, Allows mixed datatypes
print("=== Lists (Team Players) ===")

# Create a list
team_players = ["Rohit", "Kohli", "Gill", "Hardik", "Bumrah"]
print(f"Initial Team: {team_players}")

# Adding elements
team_players.append("Siraj")
print(f"After Adding a Player: {team_players}")
team_players.insert(2, "Dhoni")
print(f"After Inserting Captain: {team_players}")

# Removing elements
team_players.remove("Siraj")
print(f"After Removing a Player: {team_players}")
team_players.pop(2)
print(f"After Popping Player at Index 2: {team_players}")

# List Slicing
team_players = ["Rohit", "Kohli", "Gill", "Hardik", "Bumrah"]
print(f"Initial Team: {team_players}")
print(f"Top Order (2:4): {team_players[2:4]}")  # players from index 2 to 3

# List Comprehension
player_scores = [runs**2 for runs in range(1, 6)]
print(f"Player Scores Squared (for fun): {player_scores}")

# Tuple - Ordered, Immutable, Allows mixed datatypes
print("\n=== Tuples (Match Info) ===")

# Create a tuple
match_info = ("India vs Australia", "Final", "Ahmedabad Stadium")
print(f"Match Info: {match_info}")

# Accessing Elements
print(f"Venue: {match_info[2]}")

# Tuples are Immutable
updated_match_info = match_info + ("Evening Match",)
print(f"Updated Match Info: {updated_match_info}")

# Sets - Unordered, Mutable, No Duplicates
print("\n=== Sets (Sports Equipment) ===")

# Create a set
equipment = {"Bat", "Ball", "Gloves", "Pads"}
print(f"Initial Equipment Set: {equipment}")

# Adding elements
equipment.add("Helmet")
print(f"After Adding: {equipment}")
equipment.update(["Stumps", "Shoes"])
print(f"After Updating Multiple: {equipment}")

# Removing elements
equipment.remove("Helmet")  # throws error if not found
print(f"After Removing: {equipment}")
equipment.discard("Shoes")  # safe remove
print(f"After Discard: {equipment}")
equipment.pop()  # removes a random item
print(f"After Pop: {equipment}")
equipment.clear()  # empty the set
print(f"After Clear: {equipment}")

# Set Operations
cricket_equipment = {"Bat", "Ball", "Pads", "Helmet"}
football_equipment = {"Ball", "Goalpost", "Gloves", "Boots"}
print(f"Union: {cricket_equipment.union(football_equipment)}")
print(f"Intersection: {cricket_equipment.intersection(football_equipment)}")
print(f"Difference (Cricket - Football): {cricket_equipment.difference(football_equipment)}")
print(f"Symmetric Difference: {cricket_equipment.symmetric_difference(football_equipment)}")

# Dictionary - Unordered, Mutable, Key-Value pairs
print("\n=== Dictionaries (Player Stats) ===")

# Create a dictionary
player_stats = {
    "name": "Virat Kohli",
    "age": 35,
    "role": "Batsman"
}
print(f"Initial Player Stats: {player_stats}")

# Accessing Elements
print(f"Name: {player_stats['name']}")
print(f"Role: {player_stats.get('role')}")

# Adding & Updating elements
player_stats["runs"] = 12000
player_stats["age"] = 36
print(f"After Updating: {player_stats}")

# Removing elements
del player_stats["role"]
print(f"After Deleting Role: {player_stats}")
removed_value = player_stats.pop("age")
print(f"After Popping Age: {player_stats}, Popped Value: {removed_value}")
player_stats.clear()
print(f"After Clearing All Stats: {player_stats}")

# Dictionary Methods
player_stats = {"name": "Dhoni", "matches": 350, "runs": 10773}
keys = player_stats.keys()
values = player_stats.values()
items = player_stats.items()
print(f"Keys: {keys}, Values: {values}, Items: {items}")

# Dictionary Comprehension
player_runs = {player: player*100 for player in range(1, 6)}
print(f"Player Runs Dictionary: {player_runs}")
