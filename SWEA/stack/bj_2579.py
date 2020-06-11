num = int(input())
score=[]
anw=0

def getsome(here):
    global anw, howmany
    if here > howmany : return
    if here ==howmany:
        anw+=1
        return 
    
    getsome(here+1)
    getsome(here+2)

howmany = 3
getsome(0)

