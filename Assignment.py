rows, cols = 12, 12
Matrix=[]
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(int(input("Please enter matrix values: "))
    Matrix.append(col)
print(Matrix)
sum=0
for i in range(5):
    for j in range(i + 1, 11 - i):
        sum += Matrix[i][j]

print("The sum is: "+sum)


