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
"""


""" 
from functools import wraps

def player_start_drill(function):
    @wraps(function)
    def wraper(*args,**kwargs):
        print("🏟️ Training action starting...")
        value = function(*args,**kwargs)
        print("🏁 Training action complete.")
        return value
    return wraper

@player_start_drill
def start_drill(player, drill):
    print(f"{player} is practicing {drill}.")

start_drill("greydev","shooting") 


@player_start_drill
def start_drill(player, drill):
    print(f"{player} is practicing {drill}.")

class TrainingArea:
    def __enter__(self):
        print("🚪 Training arena opened.")
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        print(f"🧹 Cleaning training equipment.\n🔒 Training arena closed.")
    def prepare(self,drill):
         print(f"Preparing drill: {drill}")
        
players = [
    "Saka",
    "Salah",
    "Musiala",
    "Yamal"
]

drills = [
    "Passing",
    "Speed",
    "Finishing"
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
playersquad = PlayerSquad(players)

with TrainingArea() as area:
    for player in playersquad:
        for drill in training:
            area.prepare(drill)
            start_drill(player,drill) 
        for drill in training:
            area.prepare(drill)
            start_drill(player,drill) 
 """


class TrainingArea:
    def __enter__(self):
        print("🚪 Training arena opened.")
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print("oh! sorry an error occured")
        print(f"🧹 Cleaning training equipment.\n🔒 Training arena closed.")
    def prepare(self,drill):
         print(f"Preparing drill: {drill}")


with TrainingArea() as arena:
    arena.prepare("finishing")
    score = 10/0
