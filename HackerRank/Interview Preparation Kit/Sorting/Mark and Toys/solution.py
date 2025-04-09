
def maximumToys(prices, k):
    
    print("Prices:",prices)
    print(f"K: {k}")
    
    isSwapped = True
    
    while(isSwapped):
        isSwapped = False
        for i in range(len(prices)-1):
            temp = 0
            if (prices[i] > prices[i+1]):
                print("unordered, must swap!")
                temp = prices[i+1]
                prices[i+1] = prices[i]
                prices[i] = temp
                print("swapped done!")
                isSwapped = True
                
    print("final prices:", prices)
    number_of_toys = 0
    avaiable_budget = k
    for item in prices:
        if avaiable_budget <1: 
            break
        if item <= avaiable_budget:
            number_of_toys += 1
            avaiable_budget -= item
            
    print("After running last for loop")
    print("number of toys:", number_of_toys)
    print("avaiable budget:",avaiable_budget)
    return number_of_toys

if __name__ == '__main__':
  
    test_array = [1, 12, 5, 111, 200, 1000, 10]
    k = 50
    print(maximumToys(test_array,k))
    # Expected output:
    # 4
    # Explanation: 
    # He can buy toys that cost 1, 12, 5 and 10. 
    # The other toys cost more than 50 to buy.
    
    test_array_2 = [3, 7, 2, 9, 4]
    k = 15
    print(maximumToys(test_array_2,k))
    # Expected output:
    # 4
    
    test_array_3 = [1, 2, 3, 4, 5]
    k = 5
    print(maximumToys(test_array_3,k))
    # Expected output:
    # 2
    # Explanation:
    # He can buy toys that cost 1 and 2.
    # The other toys cost more than 5 to buy.