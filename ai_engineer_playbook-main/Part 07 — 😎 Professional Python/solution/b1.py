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
