#스타트와 링크
def Score(team):
    r = 0
    for i in team:
        for j in team:
            #if i!=j:
            r+=arr[i][j]
    return r

def MakeTeam(idx): 
    global teamB, anw, minn, count, maxx
    if count == maxx:
        anw = True
        return

    if len(teamA)==N//2:
        for k in range(N):
            if not visited[k]:
                teamB.append(k)

        result = abs(Score(teamA) - Score(teamB))

        if result == 0:
            anw = True
            minn = result
            return

        elif result < minn: 
            minn=result
        count+=1
        teamB = []
        return

    for t in range(idx,N):
        if not visited[t]:
            visited[t]=True
            teamA.append(t)

            MakeTeam(t)

            if anw:
                break
            visited[t]=False
            teamA.pop()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited=[False for _ in range(N)]
teamA = []
teamB = []
anw = False
count=0
temp=1
minn=987654321

for i in range(N, N//2,-1):
    temp *=i
for j in range(N//2,0,-1):
    temp//=j

maxx=temp//2
MakeTeam(0)
print(minn)