

'''
Given an array Arr of size N, print second largest element from an array.

Example 1:

Input: 
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element of the 
array is 35 and the second largest element
is 34.'''




#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		
	
		'''arr.sort
		
		for i in range(n-2,-1,-1):
		    if arr[i] != arr[n-1]:
		        return arr[i]
		    return'''
		    
		max1=arr[0]
		max2=-1
		for i in range(n):
		    if max1<arr[i]:
		        max1=arr[i]
		        
		for i in range(n):
		    if max1==arr[i]:
		        continue
		    if max2<arr[i]:
		        max2=arr[i]
		        
		return max2
	

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
