import random
import string
from cryptography.fernet import Fernet

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

def add(enc_pwd):
    with open("password.txt", "a") as f:
        f.write(enc_pwd.decode() + "\n")

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                try:
                    decrypted_passw = fernet.decrypt(line.encode()).decode()
                    print("Decrypted password:", decrypted_passw)
                except Exception as e:
                    print(f"Failed to decrypt password: {e}")

def save_key(key):
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

try:
    key = load_key()
    fernet = Fernet(key)
except FileNotFoundError:
    key = Fernet.generate_key()
    fernet = Fernet(key)
    save_key(key)

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)

enc_pwd = fernet.encrypt(pwd.encode())
answer = input("Do you want to save the password (y/n)? ")
if answer == "y":
    add(enc_pwd)

load = input("Do you want to see saved passwords (y/n)? ")
if load == "y":
    view()
else:
    print("The generated password is:", pwd)