def solution(n):
    
    left = 0
    right = 0        
        
    temp = str(n)
    condition = int(len(temp)/2)

    for i in range(condition):
        left += int(temp[i])
        right += int(temp[i+condition])

    if left == right:
        return True
    else:
        return False
