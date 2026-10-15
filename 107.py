# Problem 107: Spiral number matrix (4×4)

n = 4
matrix = []
for i in range(n):
    matrix.append([0] * n)

top = 0
bottom = n - 1
left = 0
right = n - 1
num = 1

while top <= bottom and left <= right:
    for j in range(left, right + 1):
        matrix[top][j] = num
        num = num + 1
    top = top + 1

    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num = num + 1
    right = right - 1

    for j in range(right, left - 1, -1):
        matrix[bottom][j] = num
        num = num + 1
    bottom = bottom - 1

    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num = num + 1
    left = left + 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).rjust(3), end=" ")
    print()
