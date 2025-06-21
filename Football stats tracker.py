name = input("Enter your name: ")
position = input("Enter your position: ")
matches = int(input("How many matches have you played? "))
goals = int(input("How many goals have you scored? "))

goals_per_match = goals / matches

print(f"\n{name} plays as a {position}.")
print(f"Total goals: {goals}")
print(f"Goals per match: {goals_per_match:.2f}")


assists = int(input("How many assists have you made? "))
contributions = goals + assists
contributions_per_match = contributions / matches

print(f"\n{name} plays as a {position}.")
print(f"Matches Played: {matches}")
print(f"Goals: {goals}")
print(f"Assists: {assists}")
print(f"Goal Contributions: {contributions}")
print(f"Goals per Match: {goals / matches:.2f}")
print(f"Contributions per Match: {contributions_per_match:.2f}")

wins = int(input("How many matches did you win? "))
draws = int(input("How many matches ended in a draw? "))
losses = matches - (wins + draws)

win_rate = (wins / matches) * 100

print(f"\n{name} plays as a {position}.")
print(f"Matches Played: {matches}")
print(f"Wins: {wins}, Draws: {draws}, Losses: {losses}")
print(f"Win Rate: {win_rate:.1f}%")
print(f"Goals: {goals}, Assists: {assists}")
print(f"Goal Contributions: {contributions}")
print(f"Goals per Match: {goals / matches:.2f}")
print(f"Contributions per Match: {contributions_per_match:.2f}")

while True:
    print("\n📋 My Football Tracker Menu:")
    print("1. Enter Player Stats")
    print("2. View Stats Summary")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        name = input("Enter your name: ")
        position = input("Enter your position: ")
        matches = int(input("How many matches have you played? "))
        goals = int(input("How many goals have you scored? "))
        assists = int(input("How many assists have you made? "))
        wins = int(input("How many matches did you win? "))
        draws = int(input("How many draws? "))
        losses = matches - (wins + draws)
        
        contributions = goals + assists
        goals_per_match = goals / matches
        contributions_per_match = contributions / matches
        win_rate = (wins / matches) * 100
    
    elif choice == "2":
        try:
            print(f"\n{name} plays as a {position}.")
            print(f"Matches: {matches}, Wins: {wins}, Draws: {draws}, Losses: {losses}")
            print(f"Win Rate: {win_rate:.1f}%")
            print(f"Goals: {goals}, Assists: {assists}")
            print(f"Goal Contributions: {contributions}")
            print(f"Goals per Match: {goals_per_match:.2f}")
            print(f"Contributions per Match: {contributions_per_match:.2f}")
        except:
            print("\n⚠️ You need to enter stats first (Option 1)!")
    
    elif choice == "3":
        print("🚪 Exiting My Football Tracker. See you next match!")
        break
    else:
        print("❌ Invalid choice. Please pick 1, 2, or 3.")


team = []

while True:
    print("\n📋 Team Manager Menu:")
    print("1. Add Player Stats")
    print("2. View All Players")
    print("3. Exit")

    choice = input("Pick an option (1-3): ")

    if choice == "1":
        name = input("Player name: ")
        position = input("Position: ")
        matches = int(input("Matches played: "))
        goals = int(input("Goals: "))
        assists = int(input("Assists: "))
        wins = int(input("Wins: "))
        draws = int(input("Draws: "))
        losses = matches - (wins + draws)

        contributions = goals + assists
        goals_per_match = goals / matches
        contributions_per_match = contributions / matches
        win_rate = (wins / matches) * 100print(f"✅ {name} added to the squad!")

    elif choice == "2":
        if len(team) == 0:
            print("⚠️ No players added yet.")
        else:
            for player in team:
                print("\n📊 Player Summary:")
                fr stat, value in player.items():
                    if isinstance(value, float):
                        print(f"{stat}: {value:.2f}")
                    else:
                        print(f"{stat}: {value}")

    elif choice == "3":
        print("🚀 Exiting Team Manager. Keep building your squad!")
        break
    else:
        print("❌ Invalid option. Choose 1, 2 or 3.")


            "Draws": draws,
            "Losses": losses,
            "Win Rate (%)": win_rate,
            "Goal Contributions": contributions,
            "Goals/Match": goals_per_match,
            "Contrib./Match": contributions_per_match
        }
























































