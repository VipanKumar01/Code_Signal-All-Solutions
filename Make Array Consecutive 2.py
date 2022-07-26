def solution(statues):
    temp = 0
    statues.sort()
    
    for i in range(len(statues) - 1):
        if statues[i+1] - statues[i] > 1:
            temp += statues[i+1] - statues[i] - 1
            
    return temp
