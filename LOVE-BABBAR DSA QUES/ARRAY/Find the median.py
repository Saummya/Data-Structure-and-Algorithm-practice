'''
Given an array arr[] of N integers, calculate the median
 

Example 1:

Input: N = 5
arr[] = 90 100 78 89 67
Output: 89
Explanation: After sorting the array 
middle element is the median 

Example 2:

Input: N = 4
arr[] = 56 67 30 79
Output: 61
Explanation: In case of even number of 
elements, average of two middle elements 
is the median.

'''
#User function Template for python3

class Solution:
	def find_median(self, v):
		# Code here
		n=len(v)
		v.sort()
		if n%2!=0:
		    mid=n//2
		    return v[mid]
		    
		else:
		    m1=n//2
		    m2=(n//2)-1
		    av=(v[m1]+v[m2])//2
		    return av

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends
