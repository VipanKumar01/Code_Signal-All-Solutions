def solution(matrix):
    row = len(matrix)
    col = len(matrix[0])
    sum = 0
    
    for i in range(col):
        for j in range(row):
            if matrix[j][i] == 0:
                break
            else:
                sum += matrix[j][i]
        
    return sum
