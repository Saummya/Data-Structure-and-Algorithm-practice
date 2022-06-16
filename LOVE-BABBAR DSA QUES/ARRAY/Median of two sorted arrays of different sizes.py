'''
Given two sorted arrays, a[] and b[], the task is to find the median of these sorted arrays, in O(log n + log m) time complexity, 
when n is the number of elements in the first array, and m is the number of elements in the second array. 
'''

'''
Example: 

Input: ar1[] = {-5, 3, 6, 12, 15}
        ar2[] = {-12, -10, -6, -3, 4, 10}
Output : The median is 3.
Explanation : The merged array is :
        ar3[] = {-12, -10, -6, -5 , -3,
                 3, 4, 6, 10, 12, 15},
       So the median of the merged array is 3

Input: ar1[] = {2, 3, 5, 8}
        ar2[] = {10, 12, 14, 16, 18, 20}
Output : The median is 11.
Explanation : The merged array is :
        ar3[] = {2, 3, 5, 8, 10, 12, 14, 16, 18, 20}
        if the number of the elements are even, 
        so there are two middle elements,
        take the average between the two :
        (10 + 12) / 2 = 11.
Method 1: This method uses a linear and simpler approach. 

Approach: The given arrays are sorted, so merge the sorted arrays in an efficient way and keep the count of elements inserted in the output array or printed form. So when the elements in the output array are half the original size of the given array print the element as a median element. There are two cases: 

Case 1: m+n is odd, the median is at (m+n)/2 th index in the array obtained after merging both the arrays.
Case 2: m+n is even, the median will be average of elements at index ((m+n)/2 – 1) and (m+n)/2 in the array obtained after merging both the arrays
Algorithm: 

Given two arrays are sorted. So they can be merged in O(m+n) time. Create a variable count to have a count of elements in the output array.
If the value of (m+n) is odd then there is only one median else the median is the average of elements at index (m+n)/2 and ((m+n)/2 – 1).
To merge the both arrays, keep two indices i and j initially assigned to 0. Compare the ith index of 1st array and jth index of second, increase the index of the smallest element and increase the count.
Store (m+n)/2 and (m+n)/2-1 in two variables (In the below C++ code, m1 and m2 are used for this purpose).
Check if the count reached (m+n) / 2. If (m+n) is odd return m1, If even return (m1+m2)/2.
'''

# A Simple Merge based O(n) solution to find
# median of two sorted arrays

""" This function returns median of ar1[] and ar2[].
Assumption in this function:
Both ar1[] and ar2[] are sorted arrays """
def getMedian(ar1, ar2, n, m) :

	i = 0 # Current index of input array ar1[]
	j = 0 # Current index of input array ar2[]
	m1, m2 = -1, -1

	# Since there are (n+m) elements,
	# There are following two cases
	# if n+m is odd then the middle
	# index is median i.e. (m+n)/2
	if((m + n) % 2 == 1) :
		for count in range(((n + m) // 2) + 1) :	
			if(i != n and j != m) :		
				if ar1[i] > ar2[j] :
					m1 = ar2[j]
					j += 1
				else :
					m1 = ar1[i]
					i += 1		
			elif(i < n) :		
				m1 = ar1[i]
				i += 1
		
			# for case when j<m,
			else :		
				m1 = ar2[j]
				j += 1	
		return m1
	
	# median will be average of elements
	# at index ((m + n)/2 - 1) and (m + n)/2
	# in the array obtained after merging ar1 and ar2
	else :
		for count in range(((n + m) // 2) + 1) :		
			m2 = m1
			if(i != n and j != m) :	
				if ar1[i] > ar2[j] :
					m1 = ar2[j]
					j += 1
				else :
					m1 = ar1[i]
					i += 1		
			elif(i < n) :		
				m1 = ar1[i]
				i += 1
			
			# for case when j<m,
			else :		
				m1 = ar2[j]
				j += 1	
		return (m1 + m2)//2

# Driver code	
ar1 = [900]
ar2 = [5, 8, 10, 20]

n1 = len(ar1)
n2 = len(ar2)
print(getMedian(ar1, ar2, n1, n2))

# This code is contributed by divyesh072019
