'''
Given a stream of incoming numbers, find average or mean of the stream at every point.

 

Example 1:

Input:
n = 5
arr[] = {10, 20, 30, 40, 50}
Output: 10.00 15.00 20.00 25.00 30.00 
Explanation: 
10 / 1 = 10.00
(10 + 20) / 2 = 15.00
(10 + 20 + 30) / 3 = 20.00
And so on.
 

Example 2:

Input:
n = 2
arr[] = {12, 2}
Output: 12.00 7.00 
Explanation: 
12 / 1 = 12.00
(12 + 2) / 2 = 7.00
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function streamAvg() which takes the array of integers arr and n as input parameters and returns an array of type float denoting the average at every point in the stream. 

 

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

 

Constraints:
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 106
'''
#User function Template for python3

class Solution:
	def streamAvg(self, arr, n):
		# code here
		l= []
        sm =0
        for x in range(len(arr)):
            sm+=arr[x]
            a = sm/(x+1)
            l.append(a)
        return l

		

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f'%x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
