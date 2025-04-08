def countSwaps(a):
    number_of_swaps = 0
    first_element = 0
    last_element = 0
    swapped = True
    
    print("Array:",a)
    while swapped:
        swapped = False
        for i in range(len(a)-1):
            
            temp=0
            print("item:",a[i])
            if(a[i] > a[i+1]):
                print("maior")
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp
                number_of_swaps +=1
                swapped = True
            print("current array:",a)
            
            
    first_element = a[0]   
    last_element = a[-1]  
    
    print(f"Array is sorted in {number_of_swaps} swaps.")
    print(f"First Element: {first_element}")
    print(f"Last Element: {last_element}")

if __name__ == '__main__':
  test_array = [3, 2, 1]
  countSwaps(test_array)
  # Expected output:
  # Array is sorted in 3 swaps. 
  
  test_array_2 = [1, 2, 3]
  countSwaps(test_array_2)
  # Expected output:
  # Array is sorted in 0 swaps.
  
  test_array_3 = [4, 3, 2, 1]
  countSwaps(test_array_3)
  # Expected output:
  # Array is sorted in 6 swaps.