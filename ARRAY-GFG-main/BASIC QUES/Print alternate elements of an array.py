'''
You are given an array A of size N. You need to print elements of A in alternate order (starting from index 0).

Example 1:

Input:
N = 4
A[] = {1, 2, 3, 4}
Output:
1 3
Example 2:

Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
1 3 5
Your Task:
Since this is a function problem, you just need to complete the provided function void print(int ar[],int n)'''

#User function Template for python3

# arr is the array
# n is the number of elements in array
def printAl(arr,n):
    # your code here
    l=[]
    for i in range(n):
        if i%2==0:
           print(arr[i],end=" ")
      
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        printAl(arr,n)
        print()
# } Driver Code Ends
