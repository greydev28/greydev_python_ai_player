""" players = [
    "Saka",
    "Salah",
    "Musiala",
    "Yamal"
]


class PlayerSquad:
    def __init__(self,players):
        self.players = players
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter < len(self.players):
            value = self.players[self.counter]
            self.counter+=1
            return value
        raise StopIteration
playersquad = PlayerSquad(players)

for player in playersquad:
    print(player)
 """

def training_drills():
    drills = [
        "Passing",
        "Speed",
        "Finishing",
        "Positioning"
    ]
    counter = 0
    while counter < len(drills):
        value = drills[counter]
        counter += 1
        yield value

training = training_drills()
print(next(training))
print(next(training))
print(next(training))
print(next(training))
print(next(training))