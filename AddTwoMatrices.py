# A=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# B=[[3,2,4],
#    [5,6,8],
#    [5,3,6]]
# re=[[0,0,0],
#     [0,0,0],
#     [0,0,0]]
# for i in range(len(A)):
#     for j in range(len(B)):
#         re[i][j]=A[i][j]+B[i][j]
# for r in re:
#     print(r)



#take matrix input from user
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
# A for loop for row entries
for row in range(Row): 
	a = []
	# A for loop for column entries
	for column in range(Column): 
		a.append(int(input()))
		print(a)
	matrix.append(a)



# For printing the matrix
for row in range(Row):
	for column in range(Column):
		print(matrix[row][column], end=" ")
	print()
