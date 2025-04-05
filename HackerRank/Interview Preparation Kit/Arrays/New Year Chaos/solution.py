def minimumBribe(q):
    bribes = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)

if __name__ == '__main__':
    test_1 = [2, 1, 5, 3, 4]
    minimumBribe(test_1) # 3
    test_2 = [2, 5, 1, 3, 4]
    minimumBribe(test_2) # Too chaotic
    test_3 = [5, 1, 2, 3, 7, 8, 6, 4]
    minimumBribe(test_3) # Too chaotic
    test_4 = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribe(test_4) # 7

