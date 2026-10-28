""" def show_players():
    print("show all players")

def show_teams():
    print("show all teams")

def show_stats():
    print("show all stats")

commands = {
    "players":show_players,
    "team" : show_teams,
    "stats": show_stats
}


def run_command(function):
    return function()

run_command(show_players)
commands["players"]()
commands['team']()

def training_decorator(function):
    def wraper():
        print("🏃 Training session starting...")
        function()
        print("💪 Training session complete!")
    return  wraper



# training_decorator1 = training_decorator(train_player)
# training_decorator1()

@training_decorator
def train_player():
    print("player is training!")

train_player()

def announcer(function):
    def wraper(*args,**kwargs):
        print("📢 Player announcement!")
        result = function(*args,**kwargs)
        print("📢 End of announcement")
        return result
    return wraper
@announcer
def introduce_player(name,position):
    print(f'{name} plays as a {position}')

introduce_player("saka",7)

@announcer
def add(a,b):
    print( a + b)

add(4,6) """

def tracker(function):
    def wraper(*args,**kwargs):
        result = function(*args,**kwargs)
        return result
    return wraper

@tracker
def calculate_score(goals, assists):
    return goals * 4 + assists * 3

print(calculate_score(5,8))


# debugging lab - the missing return 

def logger(function):
    def wrapper(*args, **kwargs):
        print("Running...")
        return function(*args, **kwargs)

    return wrapper


@logger
def multiply(a, b):
    return a * b


result = multiply(5, 4)

print(result)

@logger
def add_sum(a,b):
    return a + b

print(add_sum(6,5))
