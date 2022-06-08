'''
Given a sorted array Arr of size N and a value X, find the number of array elements less than or equal to X and elements more than or equal to X. 

Example 1:

Input:
N = 7, X = 0
Arr[] = {1, 2, 8, 10, 11, 12, 19}
Output: 0 7
Explanation: There are no elements less or
equal to 0 and 7 elements greater or equal
to 0.
Example 2:

Input:
N = 7, X = 5
Arr[] = {1, 2, 8, 10, 11, 12, 19}
Output: 2 5
Explanation: There are 2 elements less or
equal to 5 and 5 elements greater or equal
to 5.
Your Task:
You don't need to read input or print anything. Your task is to complete the function getMoreAndLess() which takes the array of integers arr, n and x as parameters and returns an array of size 2. pair denoting the answer. The first value is number of elements less than or equal to x and the second value is number of elements more than or equal to x.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)'''

#User function Template for python3
class Solution:

	def getMoreAndLess(self,arr, n, x):
		# code here
		c1=0
		c2=0
		l=[]
		for i in range(n):
		    if arr[i]<=x:
		        c1+=1
		    if arr[i]>=x:
		        c2+=1
		l.append(c1)
		l.append(c2)
		return l

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMoreAndLess(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends
