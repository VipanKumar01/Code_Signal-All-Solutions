from collections import Counter
def solution(s1, s2):
    
    common_letters = Counter(s1) & Counter(s2)  
    result = (sum(common_letters.values()))
    
    return result
