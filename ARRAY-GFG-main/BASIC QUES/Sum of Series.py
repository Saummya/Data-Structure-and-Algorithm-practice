'''
Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms) 

Example 1:

Input:
N = 1
Output: 1
Explanation: For n = 1, sum will be 1.
Example 2:

Input:
N = 5
Output: 15
Explanation: For n = 5, sum will be 1
+ 2 + 3 + 4 + 5 = 15.
Your Task:
Complete the function seriesSum() which takes single integer n, as input parameters and returns an integer denoting the answer. You don't to print answer or take inputs.'''

#User function Template for python3
class Solution:

	
	def seriesSum(self,n):
	    # code here
	    sum_total=n*(n+1)/2
	    return int(sum_total)


#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.seriesSum(n)
        print(ans)
        tc=tc-1
# } Driver Code Ends
