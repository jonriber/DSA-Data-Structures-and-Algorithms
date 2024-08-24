import itertools
import string

# define the charset to be used
# this is a combination of lowercase letters and digits
charset = string.ascii_lowercase + string.digits

#define our password to be cracked
#On real scenarios, this would be unknown and the main goal of the script
password = "abc123"


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
  brute_force(password, charset)






