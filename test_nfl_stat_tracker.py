import unittest

# Simulated version of your Player class and player data
class Player:
    def __init__(self, name, position, stats, trivia_question, trivia_answer):
        self.name = name
        self.position = position
        self.stats = stats
        self.trivia_question = trivia_question
        self.trivia_answer = trivia_answer

    def get_stat(self, stat):
        return self.stats.get(stat.lower(), "Stat not found.")

players = {
    "terry mclaurin": Player("Terry McLaurin", "WR", {
        "receptions": 82, "yards": 1096, "touchdowns": 13
    }, "How many touchdowns did Terry score in 2024?", "13")
}

class TestNFLStatTracker(unittest.TestCase):
    def test_player_stat_retrieval(self):
        terry = players["terry mclaurin"]
        self.assertEqual(terry.get_stat("receptions"), 82)
        self.assertEqual(terry.get_stat("yards"), 1096)
        self.assertEqual(terry.get_stat("touchdowns"), 13)
        self.assertEqual(terry.get_stat("invalid"), "Stat not found.")

    def test_trivia_answer(self):
        terry = players["terry mclaurin"]
        self.assertEqual(terry.trivia_answer, "13")

if __name__ == "__main__":
    unittest.main()
