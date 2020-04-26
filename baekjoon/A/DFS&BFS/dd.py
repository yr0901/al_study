def solution(dartResult):
    answer = 0
    temp = []
    bonus = ['S', 'D', 'T']
    i=0
    dartResult =list(dartResult)
    while i <len(dartResult):
        try:
            dartResult[i] = int(dartResult[i])
            temp.append(dartResult[i]**(bonus.index(dartResult[i+1])+1))
            i+=2
        except ValueError:
            if len(temp)==1:
                temp[-1]*=2 
            else:
                temp[-1]*=2
                temp[-2]*=2
            i+=1
    answer = sum(temp)
    
    return answer

print(solution('1S2D*3T'))
