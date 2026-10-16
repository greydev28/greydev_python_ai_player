class Player:
    def __init__(self,name,age,position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"my is {self.name}\ni am,{self.age}\ni play {self.position} "