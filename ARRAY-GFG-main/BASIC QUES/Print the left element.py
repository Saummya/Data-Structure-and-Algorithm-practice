'''
Given a array of length N, at each step it is reduced by 1 element. In the first step the maximum element would be removed, while in the second step minimum element of the remaining array would be removed, in the third step again the maximum and so on. Continue this till the array contains only 1 element. And find the final element remaining in the array.

 

Example 1:

Input:
N = 7
A[] = {7, 8, 3, 4, 2, 9, 5}
Ouput:
5
Explanation:
In first step '9' would be removed, in 2nd step
'2' will be removed, in third step '8' will be
removed and so on. So the last remaining
element would be '5'.  
 

Example 2:

Input:
N = 8
A[] = {8, 1, 2, 9, 4, 3, 7, 5}
Ouput:
4
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function leftElement() which takes the array A[] and its size N as inputs and returns the final remaining element in the array.


Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)

 

Constraints:
1 ≤ N ≤ 106
1 ≤ Ai ≤ 1000'''

#User function Template for python3

class Solution:
    def leftElement(self, arr, n):
    # Your code goes here  
        arr.sort()
        if n==1:
            return arr[0]
        if n%2!=0:
            return arr[(n-1)//2]
        else:
            return arr[(n-1)//2]
            
    
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.leftElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
