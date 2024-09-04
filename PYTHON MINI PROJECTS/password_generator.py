import random
import string

def generate_password(min_length, numbers = True, special_character = True):
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation

  characters = letters
  if numbers:
    characters += digits
  if special_character:
    characters += special

  pwd = ""
  meets_criteria = False
  has_number = False
  has_special = False

  while not meets_criteria or len(pwd) < min_length:
    new_char = random.choice(characters)
    pwd += new_char

    if new_char in digits:
      has_number = True
    elif new_char in special:
      has_special = True
    
    meets_criteria = True
    if numbers:
      meets_criteria = has_number
    if special_character:
      meets_criteria = meets_criteria and has_special

  return pwd

def add():
  with open ("password.txt", "a") as f:
    f.write(pwd + "\n")

  
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have a numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
answer = input("Do you want to save password (y/n)? ")
if answer == "y":
  add()
else:
  print("The generated password is:", pwd)