import random

def sqrt(x):
    lastguess= x/2.0
    while lastguess!=0:
        guess= (lastguess + x/lastguess)/2
        if abs(guess - lastguess) < .000001: 
            return guess
        lastguess= guess

def Center(k):
    centers = {}
    cluster={}
    for i in range(k):
        x = random.randint(0,100)
        y = random.randint(0,100)
        center=(x,y)
        centers[i]=center
        cluster[(x,y)]=[]
    return centers , cluster

def dist1(k,points):
    dis1,mindis=0,0
    flag=True
    while dis1!=mindis or flag==True:
        flag=False
        centers,cluster=Center(k)
        dis1=0
        for p in points:
            disdict={}
            for c in range(len(centers)):
                xp,yp=p[0],p[1]
                xc,yc=centers[c]
                d=sqrt((xc-xp)**2+(yc-yp)**2)
                disdict[c]=d
            for i in disdict.keys():
                if disdict[i]==min(disdict.values()):
                    dis1+=disdict[i]
                    flag1=True
                    if dis1<mindis or flag1==True:
                        Flag1=False
                        mindis=dis1
                    for j in cluster.keys():
                        if j==centers[i]:
                            cluster[j]+=[(xp,yp)]
        
    return cluster

