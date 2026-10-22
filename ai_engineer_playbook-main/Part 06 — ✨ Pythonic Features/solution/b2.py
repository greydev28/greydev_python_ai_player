""" def football_positions():
    yield "Goalkeeper"
    yield "Defender"
    yield "Midfielder"
    yield "Forward"

positions = football_positions()
print(next(positions))
print(next(positions))
print(next(positions))


def colors():
    yield "orange"
    yield "red"
    yield "green"
    yield "yellow"

color = colors()
print(next(color))
print(next(color))
print(next(color))


def number_generator(limit):
    current_number = 0
    while current_number <= limit:
          value = current_number
          current_number+=1
          yield value
    raise StopIteration

number = number_generator(10)
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
 """

def even_numbers(limit):
    current_number = 1
    while current_number <= limit:
        if current_number % 2 != 0:
            current_number+=1
            continue
        else:
            value = current_number
            current_number+=1
            yield value 
    raise StopIteration

even_num = even_numbers(10)
print(next(even_num))
print(next(even_num))
print(next(even_num))
print(next(even_num))
print(next(even_num))


players = [
    {"name": "Salah", "position": "RW"},
    {"name": "Rice", "position": "CM"},
    {"name": "Saka", "position": "RW"},
    {"name": "Palmer", "position": "AM"},
]


def filer_position(players,position):
   for player in players:
       if player['position'] == position:
           yield player
filerposition = filer_position(players,"RW")
print(next(filerposition))

def match_events(time,event,player):
    yield{
        "minute":time,
        "event": event,
        "player": player
    }

match1 = match_events(12,"red","ramos")
match2 = match_events(27,"goal","saka")
matches = [
    match1,
    match2
    
]
print(next(match1))
print(next(match2))