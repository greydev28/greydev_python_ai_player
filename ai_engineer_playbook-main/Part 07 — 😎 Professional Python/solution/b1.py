# try:
#    goals = int(input("Enter training duration in minutes: "))
#    divid = 10 / goals
# except ValueError:
#    print("⚠️ Please enter valid numbers.")
# except ZeroDivisionError:
#    print("⚠️ You cannot divide by zero.")
# else:
#    print(f"🏃 Training duration recorded.{goals}")
# finally: 
#    print("Done!")


# try:
#    jersey_number = int(input("please a jersey_number: "))
# except ValueError:
#    print("⚠️ Please enter valid numbers ")
# else:
#    print(f"⚽ Player number accepted with jersy No. {jersey_number} ")
# finally:
#    print("📋 Registration attempt complete.")


# ValueError
# TypeError
# ZeroDivisionError
# IndexError
# KeyError
# FileNotFoundError
# NameError


""" def set_player_age(age):
   try:
      int_age=int(age)
   except ValueError:
      raise ValueError("Age must be an integer")
   
   if int_age < 0:
      raise ValueError("number cannot be less than zero! ")

   return int_age

try:
   set_player_age(-1)
except ValueError as err:
   print(err)
 """
# def set_player_age(age):
#    try:
#      int_age = int(age)
#    except ValueError:
#       print("age must be a positive number!")

#    if int_age < 0:
#       raise ValueError("age not be a none integer ")
#    else:
#       print(int_age)

# try:
#    set_player_age()
# except ValueError as err:
#    print(err)
# finally:
#       print("i'm done!")

""" def set_player_age(age):
    int_age = int(age)
    if not int_age:
         raise ValueError("not a valid number")
    if age < 0:
         print("age can not be less 0.")
    return age
try:
    print(set_player_age(20))
except ValueError as err:
    print(err)

 """
""" 
def save_to_database(name,score):
   profile = {
        "name": name,
        "score": score
    }
   return profile 

def send_email(name):
    return f"hello mr {name} you were selected"

def checking_student():
      name = input("Name: ")
      age = int(input("Age: "))
      score = 100 / age
      print(f"{name}: {score}")
      print(save_to_database(name, score))
      print(send_email(name))
    
    
try:
   checking_student()
except ValueError:
    print("Something went wrong.")
except ZeroDivisionError:
    print("sorry age can not be 0")   
finally:
    print("thank!")
 """
""" import json

class PlayerData(Exception):
    pass

def load_player_data():
   try:
      with open("data/file", "r")as file:
         json.load(file)
   except FileNotFoundError as error:
       raise PlayerData("Player data cannot be found!") from error

try:
    load_player_data()
except PlayerData as e:
    print(e) """
class RegistrationError(Exception):
    pass



def register_player(name,age,position):
      # Validate name
   if not name.strip():
      raise RegistrationError("Name cannot be empty.")
   if len(name) < 3:
      raise RegistrationError("Sorry name cannot be empty")
   # Validate age
   try:
      age = int(age)
   except (ValueError, TypeError) as error:
      raise RegistrationError("Age must be a valid number.") from error

   if age < 16:
      raise RegistrationError("Age cannot be less than 16.")

   # Validate position
   valid_positions = ("forward", "midfielder", "defender", "goalkeeper")

   position = position.strip().lower()

   if position not in valid_positions:
      allowed = ", ".join(valid_positions)
      raise RegistrationError(f"Invalid player position. Choose from: {allowed}.")
   position = position.title()
   # Successful registration
   return {
      "name": name,
      "age": age,
      "position": position
   }



try:
    player = register_player("greydev","kj","Midfielde")
except RegistrationError as err:
    print(err)
except TypeError as err:
    print(err)
else:
    print(player)



# try
#  ↓
# Attempt risky operation

# except
#  ↓
# Handle expected failure

# else
#  ↓
# Handle successful execution

# finally
#  ↓
# Guarantee cleanup

# raise
#  ↓
# Signal an invalid condition

# custom exceptions
#  ↓
# Give domain-specific meaning

# exception propagation
#  ↓
# Let errors travel to
# the layer that can handle them

# challenge 
import json

class FileData(Exception):
    pass
def file_backed():
   try: 
      with open("file","r") as file:
         json.load(file)
   except  FileNotFoundError as error:
      raise FileData("file not found!") from error


try:
   file_backed()
except FileData as err:
   print(err)

