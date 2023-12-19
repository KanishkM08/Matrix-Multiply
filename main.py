ch = int(input("Multiplying two (1.)square matrices or (2.)rectangular matrices? (1/2): "))

# get the dimensions of square matrices
if ch == 1:
    n = int(input("Enter square matrices order(nxn): "))
    r,c,r2,c2=n,n,n,n
    
elif ch == 2:
    r = int(input("Enter no. of rows of first matrix: "))
    c = int(input("Enter no. of columns of first matrix:"))
    r2 = int(input("Enter no. of rows of second matrix: "))
    c2 = int(input("Enter no. of columns of second matrix:"))
    
    # check if the matrices can be multiplied
    if c!=r2:
        print("The given confirguration is not valid to multiply two matrices")
        exit()
        
else:
    print("Please enter valid number")

# get the elements of the first matrix
print("Enter the elements of the first matrix:")
matrix1 = [[int(input()) for x in range(c)] for y in range(r)]
# Print the first matrix
print("The first matrix entered:")
for row in matrix1:
    print(row)
print("order: ",r,"x",c)

# get the elements of the second matrix
print("Enter the elements of the second matrix:")
matrix2 = [[int(input()) for x in range(c2)] for y in range(r2)]
# Print the second matrix
print("The second matrix entered:")
for row in matrix2:
    print(row)
print("order: ",r2,"x",c2)

# create a new matrix to store the result
matrix = []

# Multiplying and adding
for i in range(r):
        row = []
        for j in range(c2):
            sum = 0
            for k in range(c):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        matrix.append(row)
            
# Print the result matrix
print("The result of the multiplication is:")
for row in matrix:
    print(row)
