
#first attempt
def repeatedString(s, n):
    # Write your code here
    if len(s) <1 | n < 1 :
        return 0
    print("input s:",s)
    print("input n:",n)
    
    #testing s.len
    print("length of s:",len(s))
    s_len = len(s)
    print("testing divisor:",n%s_len)
    repeat_s = n//s_len
    print("Repeat:",repeat_s)
    left_s = n%s_len
    print("left s:",left_s)
    char_match = 0
    left_char_match = 0
    for _ in range(left_s):
        if s[_] == 'a':
            left_char_match+=1
    for _ in s:
        if _ == 'a':
            print("it is equal to a")
            char_match+=1
    total = (repeat_s*char_match) + left_char_match
    return total

if __name__ == "__main__":
  pass