// Name = Vipan Kumar
// GitHub user name = @VipanKumar01

int solution(vector<int> inputArray) {
    int dif=0;
    int max=0;
    
    for (int i=0;i<inputArray.size()-1;i++){
        dif = inputArray[i]-inputArray[i+1];
        dif = abs(dif);
        if (dif>max){
            max = dif;
        }
    }
    return max;
}


// --Happy Code--
