# trying closures in python

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Creating closures
times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)



if __name__ == '__main__':
    # expected: 27
    print(times3(9))

    # expected: 15
    print(times5(3))

    # expected: 30
    print(times5(times3(2)))