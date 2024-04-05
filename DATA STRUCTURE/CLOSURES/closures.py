# trying closures in python

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Criação de closures
times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)



if __name__ == '__main__':
    # Saída: 27
    print(times3(9))

    # Saída: 15
    print(times5(3))

    # Saída: 30
    print(times5(times3(2)))