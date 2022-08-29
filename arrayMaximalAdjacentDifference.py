# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

def solution(inputArray):
    dif = 0
    max = 0
    for i in range(len(inputArray)-1):
        dif = inputArray[i] - inputArray[i+1]
        dif = abs(dif)
        if(dif > max):
            max = dif
    return max

  # --Happy Code--
