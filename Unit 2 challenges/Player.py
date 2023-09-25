class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def play(self):
        print(f"{self.name} is playing.")

    def __str__(self):
        return f"Player Name: {self.name}\nScore: {self.score}\nStatus: Playing"

player1 = Player("Alice", 10)
player2 = Player("Bob", 20)

player1.play()
player2.play()

print(player1)
print(player2)