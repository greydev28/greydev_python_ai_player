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



# challenge

import io

def read_large_file(file_obj):
    """Step 1: Yields raw lines one by one from the file source."""
    for line in file_obj:
        # Removes trailing newlines/whitespace
        cleaned_line = line.strip()
        if cleaned_line:  # Skip empty lines
            yield cleaned_line

def filter_records(lines):
    """Step 2: Filters out header rows or comment lines lazily."""
    for line in lines:
        if not line.startswith("#") and "ID,Name" not in line:
            yield line

def transform_fields(records):
    """Step 3: Parses CSV strings into structured dictionaries."""
    for record in records:
        fields = record.split(",")
        # Example schema: ID, Name, Department, Revenue
        yield {
            "id": fields[0],
            "name": fields[1],
            "dept": fields[2],
            "revenue": float(fields[3])
        }

def compute_summary(data_pipeline):
  
    total_revenue = 0.0
    record_count = 0
    
    # This loop triggers the evaluation of the upstream generators
    for item in data_pipeline:
        total_revenue += item["revenue"]
        record_count += 1
        
    return {
        "total_records_processed": record_count,
        "total_revenue": total_revenue,
        "average_revenue": total_revenue / record_count if record_count > 0 else 0
    }

# --- Execution Example ---
# Simulating a massive 4-line file using StringIO (acts exactly like an open file)
mock_large_file = io.StringIO(
    "# Department Revenue Report\n"
    "ID,Name,Department,Revenue\n"
    "1,Alice,Engineering,150000\n"
    "2,Bob,Marketing,85000\n"
    "3,Charlie,Engineering,120000\n"
)

# 1. Chain the generators together (No data is read or processed yet!)
raw_lines = read_large_file(mock_large_file)
valid_lines = filter_records(raw_lines)
parsed_data = transform_fields(valid_lines)

# 2. Drive the pipeline to get the final result
summary = compute_summary(parsed_data)
print(summary)
# Output: {'total_records_processed': 3, 'total_revenue': 355000.0, 'average_revenue': 118333.33333333333}
