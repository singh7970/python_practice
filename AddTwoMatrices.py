# row=int(input("Enter the row number"))
# col=int(input("Enter the column number"))
# matrix=[]
# for i in range(row):
#     tem=[]
#     for j in range(col):
#         tem.append(int(input))
# matrix.append(tem)	

# for i in range(row):
#     for j in range(col):
#         print(matrix[i][j],end='')
# print( )	



# row = int(input("Enter the number of rows: "))
# col = int(input("Enter the number of columns: "))
# matrix = []

# for i in range(row):
#     temp = []
#     for j in range(col):
#         temp.append(int(input()))
#     matrix.append(temp)

# # For printing the matrix
# for i in range(row):
#     for j in range(col):
#         print(matrix[i][j], end=' ')
#     print()
row=int(input("enter the row"))
col=int(input("enter the col"))
mat=[]
for i in range(row):
    t=[]
    for j in range(col):
        t.append(int(input()))
    mat.append(t)    

# for pirnting
for i in range(row):
    for j in range(col):
        print(mat[i][j],end="  ")
    print()      

