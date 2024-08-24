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
  return ("Password not found")

if __name__ == "__main__":
  
  parser = argparse.ArgumentParser(description="Brute force password cracker")
  parser.add_argument("password", help="The password to crack")
  parser.add_argument("charset_option", choices=['1', '2'], help="Escolha '1' para letras minúsculas ou '2' para dígitos.")
  args = parser.parse_args()
  charset = get_charset(args.charset)
  password = args.password
  
  brute_force(password, charset)






