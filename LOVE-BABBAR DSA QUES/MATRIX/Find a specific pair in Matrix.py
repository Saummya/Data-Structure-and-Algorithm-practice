'''
Given an n x n matrix mat[n][n] of integers, find the maximum value of mat(c, d) – mat(a, b) over all choices of indexes such that both c > a and d > b.
Example: 

Input:
mat[N][N] = {{ 1, 2, -1, -4, -20 },
             { -8, -3, 4, 2, 1 }, 
             { 3, 8, 6, 1, 3 },
             { -4, -1, 1, 7, -6 },
             { 0, -4, 10, -5, 1 }};
Output: 18
The maximum value is 18 as mat[4][2] 
- mat[1][0] = 18 has maximum difference. 
The program should do only ONE traversal of the matrix. i.e. expected time complexity is O(n2)



A simple solution would be to apply Brute-Force. For all values mat(a, b) in the matrix, we find mat(c, d) that has maximum value such that c > a and d > b and keeps on updating maximum value found so far. We finally return the maximum value.
Below is its implementation. 
'''

# A Naive method to find maximum
# value of mat[d][e] - mat[a][b]
# such that d > a and e > b
N = 5

# The function returns maximum
# value A(d,e) - A(a,b) over
# all choices of indexes such
# that both d > a and e > b.
def findMaxValue(mat):
	
	# stores maximum value
	maxValue = 0

	# Consider all possible pairs
	# mat[a][b] and mat[d][e]
	for a in range(N - 1):
		for b in range(N - 1):
			for d in range(a + 1, N):
				for e in range(b + 1, N):
					if maxValue < int (mat[d][e] -
									mat[a][b]):
						maxValue = int(mat[d][e] -
									mat[a][b]);

	return maxValue;

# Driver Code
mat = [[ 1, 2, -1, -4, -20 ],
	[ -8, -3, 4, 2, 1 ],
	[ 3, 8, 6, 1, 3 ],
	[ -4, -1, 1, 7, -6 ],
	[ 0, -4, 10, -5, 1 ]];
		
print("Maximum Value is " +
	str(findMaxValue(mat)))
	
# This code is contributed
# by ChitraNayal

