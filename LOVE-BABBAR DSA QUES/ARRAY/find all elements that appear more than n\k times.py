'''

Given an array of size n, find all elements in array that appear more than n/k times. 
For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. 
Note that size of array is 8 (or n = 8), so we need to find all elements that appear more than 2 (or 8/4) times. 
There are two elements that appear more than two times, 2 and 3.

'''
def morethanNbyK(arr, n, k) :
    x = n // k
      
    # unordered_map initialization
    freq = {}
  
    for i in range(n) :   
        if arr[i] in freq :
            freq[arr[i]] += 1
        else :
            freq[arr[i]] = 1
        
    # Traversing the map
    for i in freq :
          
        # Checking if value of a key-value pair
        # is greater than x (where x=n/k)
        if (freq[i] > x) :
              
            # Print the key of whose value
            # is greater than x
            print(i)
