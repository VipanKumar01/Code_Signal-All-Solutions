def solution(a):

    count = 0
    Nag_Indx = []
    for i in a:
        if i == -1:
            Nag_Indx.append(count)
        count += 1
    a.sort()
    for i in range(len(Nag_Indx)):
        a.pop(0)
    for i in Nag_Indx:
        a.insert(i,-1)
        
    return a
  
