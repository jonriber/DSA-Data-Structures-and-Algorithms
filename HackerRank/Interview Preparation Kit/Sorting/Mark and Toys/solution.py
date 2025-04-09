def maximumToys(prices, k):
    # Handle edge cases
    if not prices or k <= 0:
        return 0  # No toys can be bought if prices list is empty or budget is zero/negative

    # Sort prices using Python's built-in sorting for efficiency
    prices.sort()

    number_of_toys = 0
    available_budget = k

    for item in prices:
        if item > available_budget:
            break  # Stop if the current item exceeds the remaining budget
        number_of_toys += 1
        available_budget -= item

    return number_of_toys

if __name__ == '__main__':
    test_array = [1, 12, 5, 111, 200, 1000, 10]
    k = 50
    print(maximumToys(test_array, k))
    # Expected output:
    # 4
    # Explanation: 
    # He can buy toys that cost 1, 12, 5 and 10. 
    # The other toys cost more than 50 to buy.
    
    test_array_2 = [3, 7, 2, 9, 4]
    k = 15
    print(maximumToys(test_array_2, k))
    # Expected output:
    # 4
    
    test_array_3 = [1, 2, 3, 4, 5]
    k = 5
    print(maximumToys(test_array_3, k))
    # Expected output:
    # 2
    # Explanation:
    # He can buy toys that cost 1 and 2.
    # The other toys cost more than 5 to buy.

    # Additional edge case tests
    print(maximumToys([], 10))  # Expected output: 0 (empty prices list)
    print(maximumToys([1, 2, 3], 0))  # Expected output: 0 (zero budget)
    print(maximumToys([1, 2, 3], -5))  # Expected output: 0 (negative budget)
    print(maximumToys([10, 20, 30], 5))  # Expected output: 0 (all items exceed budget)