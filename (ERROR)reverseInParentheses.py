# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

""" 
That have some Error I can't find Out. So Please Help me for solve this Questions

Samples =>

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""


def solution(inputString):
    
    countParentheses = 0
    result = ""
    temp = ""
    
    for i in range(len(inputString)):
        if inputString[i] != "(":
            result = result + (inputString[i])
        else:
            i+=1
            
            while(inputString[i] != ")"):
                temp = inputString[i] + temp
            else:
                i+=1
        result = result + temp
    return result
                
                
# --HappyCode--
