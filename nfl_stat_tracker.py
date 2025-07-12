import re  # Module 8: Regular Expressions

# Module 4, 5, 6: Object-Oriented Programming and Data Types
class Player:
    def __init__(self, name, position, stats, trivia_question, trivia_answer):
        self.name = name
        self.position = position
        self.stats = stats
        self.trivia_question = trivia_question
        self.trivia_answer = trivia_answer

    def get_stat(self, stat):  # Module 7: Advanced OOP - Class method
        return self.stats.get(stat.lower(), "Stat not found.")

# Module 5: Dictionary of player objects (also mimics a basic data store - Module 11)
players = {
    "terry mclaurin": Player("Terry McLaurin", "WR", {
        "receptions": 82,
        "yards": 1096,
        "touchdowns": 13
    }, "How many touchdowns did Terry score in 2024?", "13"),

    "jahan dotson": Player("Jahan Dotson", "WR", {
        "receptions": 19,
        "yards": 216,
        "touchdowns": 0
    }, "Did Jahan score any touchdowns in 2024?", "0"),

    "brian robinson": Player("Brian Robinson Jr.", "RB", {
        "rushing attempts": 187,
        "rushing yards": 799,
        "rushing touchdowns": 8
    }, "How many rushing touchdowns did Brian have in 2024?", "8"),

    "antonio gibson": Player("Antonio Gibson", "RB", {
        "rushing attempts": 120,
        "rushing yards": 538,
        "rushing touchdowns": 1
    }, "What was Antonio’s rushing yard total in 2024?", "538"),

    "jayden daniels": Player("Jayden Daniels", "QB", {
        "passing yards": 3568,
        "passing touchdowns": 25,
        "rushing yards": 891,
        "rushing touchdowns": 6
    }, "How many total touchdowns (passing + rushing) did Jayden have in 2024?", "31"),
}

# Module 1, 2: Python Fundamentals - input/output, conditionals, loops
def main():
    print("Welcome to the 2024 Washington Commanders NFL Stat Tracker.")
    name = input("What is your name? ")
    print(f"\nHello, {name}. This tracker is based on the 2024 NFL season.\n")

    while True:
        print("Which player's stats would you like to view?")
        for i, player_name in enumerate(players.keys(), start=1):
            print(f"{i}. {player_name.title()}")

        player_input = input("\nEnter player name: ").lower().strip()

        # Module 8: Regular Expression cleanup
        player_input = re.sub(r"[^a-zA-Z\s]", "", player_input)

        if player_input in players:
            player = players[player_input]

            print(f"\nAvailable stats for {player.name}:")
            for stat in player.stats:  # Module 6: Loop through dictionary keys
                print(f"- {stat.title()}")

            stat_input = input("\nWhich stat would you like to view? ").lower().strip()

            if stat_input in player.stats:
                print(f"\n{player.name}'s {stat_input.title()}: {player.get_stat(stat_input)}\n")
            else:
                print("That stat is not available for this player.\n")

            # Trivia Question - Part of enhanced interactivity
            print(f"Trivia: {player.trivia_question}")
            user_answer = input("Your guess: ").strip()

            if user_answer.lower() == player.trivia_answer.lower():
                print("Correct.\n")
            else:
                print(f"Incorrect. The correct answer is {player.trivia_answer}.\n")

            input("Press Enter to continue...")
        else:
            print("Player not found. Please enter a valid name.\n")

        again = input("Would you like to view another stat? (yes/no): ").lower()
        if again != "yes":
            print(f"\nThanks for using the tracker, {name}.")
            break

# Module 1: Entry point to run the script
if __name__ == "__main__":
    main()

