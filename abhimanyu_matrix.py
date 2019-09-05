# Python3 program to print 
# given matrix in spiral form 
import numpy as np 

R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 


print("Enter the entries in a single line (separated by space): ") 

# User input of entries in a 
# single line separated by space 
entries = list(map(int, input().split())) 

# For printing the matrix 
a = np.array(entries).reshape(R, C) 
print(a) 
 
def spiralPrint(m, n, a) : 
	k = 0; l = 0

	''' k - starting row index 
		m - ending row index 
		l - starting column index 
		n - ending column index 
		i - iterator '''
	

	while (k < m and l < n) : 
		
		# Print the first row from 
		# the remaining rows 
		for i in range(l, n) : 
			print(a[k][i], end = " ") 
			
		k += 1

		# Print the last column from 
		# the remaining columns 
		for i in range(k, m) : 
			print(a[i][n - 1], end = " ") 
			
		n -= 1

		# Print the last row from 
		# the remaining rows 
		if ( k < m) : 
			
			for i in range(n - 1, (l - 1), -1) : 
				print(a[m - 1][i], end = " ") 
			
			m -= 1
		
		# Print the first column from 
		# the remaining columns 
		if (l < n) : 
			for i in range(m - 1, k - 1, -1) : 
				print(a[i][l], end = " ") 
			
			l += 1

# Driver Code 
#a = [ [1, 2, 3, 4, 5, 6], 
	#[7, 8, 9, 10, 11, 12], 
	#[13, 14, 15, 16, 17, 18] ] 
spiralPrint(R, C, a) 

# This code is contributed by Amit Rathore. 
