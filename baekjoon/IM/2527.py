for tc in range(4):
    tlist=list(map(int, input().split()))
    list1=tlist[:4]
    list2=tlist[4:]
    
    w1=list1[2]-list1[0]
    h1=list1[3]-list1[1]
    w2=list2[2]-list2[0]
    h2=list2[3]-list2[1]

    xmax=ymax=0
    xmin=ymin=987654321

    for i in range(len(tlist)):
        if i&1:
            if tlist[i]>ymax:
                ymax=tlist[i]
            if tlist[i]<ymin:
                ymin=tlist[i]
        else:
            if tlist[i]>xmax:
                xmax=tlist[i]
            if tlist[i]<xmin:
                xmin=tlist[i]            
    mw=xmax-xmin
    mh=ymax-ymin

    if w1+w2>mw and h1+h2>mh:
        anw='a'
    elif w1+w2==mw and h1+h2==mh:
        anw='c'
    elif w1+w2==mw or h1+h2==mh:
        anw='b'
    else: anw='d'

    print(anw)

    
        

    

        
    
    
