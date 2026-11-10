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

def set_player_age(age):
    if not isinstance(age,int):
         raise ValueError("not a valid number")
    if age < 0:
         print()
    return age
try:
    print(set_player_age(20))
except ValueError as err:
    print(err)