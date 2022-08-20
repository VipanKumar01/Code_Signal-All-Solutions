def solution(inputString):
  
# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

""" 
That have some Error I can't find Out. So Please Help me for solve this Questions
################################################################################################################# 
    temp = set(inputString)
    
    actualLength = len(inputString)
    setLength = len(temp)
    
    if setLength == (actualLength/2) or setLength == ((actualLength//2)+1):
        return True
    else:
        return False
    """
################################################################################################################# 
    
    # a = sorted(inputString)[::2]
    # b = sorted(inputString)[1::2]
    # return b == a[:len(b)]
    
    
################################################################################################################# 
   
    string = list(inputString)
    n = len(string)
    s_set= set(string)

    from collections import Counter

    dic = Counter(string)

    k =0 #counter for odd characters

    for char in s_set:
        if dic.get(char)%2!=0:
            k+=1

    if k>1:
        return False
    else:
        return True
