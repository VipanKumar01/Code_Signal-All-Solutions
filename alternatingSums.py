# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

def solution(a):
    
    team1 = 0
    team2 = 0
    result = []
    for i in range(len(a)):
        if i%2 == 1:
            team1 = team1 + a[i]
        else:
            team2 = team2 + a[i]
            
    result.append(team2)
    result.append(team1)

    return result
            

# --HappyCode--
