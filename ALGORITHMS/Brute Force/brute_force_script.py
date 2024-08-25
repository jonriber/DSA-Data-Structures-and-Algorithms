import itertools
import string
import argparse

# define the charset to be used
# this is a combination of lowercase letters and digits
# charset = string.ascii_lowercase + string.digits

#define our password to be cracked
#On real scenarios, this would be unknown and the main goal of the script
# password = "abc"


def get_charset(option):
  if option == '1':
    return string.ascii_lowercase
  elif option == '2':
    return string.digits
  else:
    raise ValueError("Invalid input")
  
def brute_force(password, charset):
  for length in range(1, len(password)+1):
    for attempt in itertools.product(charset, repeat=length):
      attempt = "".join(attempt)
      print(f"Trying {attempt}")
      if attempt == password:
        print(f"Password has been cracked! It was {attempt}")
        return attempt
  print("Password not found")
  print("- - - - - ")
  print("- - - -  ")
  print("- - -  ")
  print("- -  ")
  print("- ")
  
  return ("Password not found")

if __name__ == "__main__":
  
  while True:
    password = input("Enter the password to crack: ")
    print("Choose charset option:")
    print("1: Lowercase letters")
    print("2: Digits")
    charset_option = input("Enter your choice (1 or 2): ")

    try:
        charset = get_charset(charset_option)
    except ValueError as e:
        print(e)
        continue

    brute_force(password, charset)

    again = input("Type 'exit' to quit or press Enter to run again: ")
    if again.lower() == 'exit':
        break






