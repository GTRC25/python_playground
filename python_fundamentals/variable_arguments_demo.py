# =========================
# 1) Football Examples
# =========================

# Example 1: *args - players who scored
def football_goals_scored(*players):
    print("Football - Goals scored by:")
    for player in players:
        print("-", player)
    print()

football_goals_scored("Messi", "Ronaldo", "Neymar")

# Example 2: **kwargs - goals per player
def football_goals_details(**player_goals):
    print("Football - Goals per player:")
    for player, goals in player_goals.items():
        print(f"{player} scored {goals} goals")
    print()

football_goals_details(Messi=2, Ronaldo=1, Neymar=3)

# =========================
# 2) BTC (Crypto) Examples
# =========================

# Example 1: *args - multiple wallet balances
def btc_check_wallets(*wallet_balances):
    print("BTC - Wallet balances:")
    for i, balance in enumerate(wallet_balances, start=1):
        print(f"Wallet {i}: {balance} BTC")
    print()

btc_check_wallets(1.5, 2.0, 0.75)

# Example 2: **kwargs - wallet balances by owner
def btc_wallet_balances(**wallets):
    print("BTC - Wallet balances by owner:")
    for owner, balance in wallets.items():
        print(f"{owner} has {balance} BTC")
    print()

btc_wallet_balances(Alice=1.5, Bob=2.0, Charlie=0.75)

# =========================
# 3) Basketball Examples
# =========================

# Example 1: *args - players in the game
def basketball_game_players(*players):
    print("Basketball - Players in the game:")
    for player in players:
        print("-", player)
    print()

basketball_game_players("LeBron", "Curry", "Durant")

# Example 2: **kwargs - points scored per player
def basketball_player_points(**points):
    print("Basketball - Points per player:")
    for player, pts in points.items():
        print(f"{player} scored {pts} points")
    print()

basketball_player_points(LeBron=30, Curry=25, Durant=28)
