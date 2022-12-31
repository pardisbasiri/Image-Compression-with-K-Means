import random

def sqrt(x):
    lastguess= x/2.0
    while lastguess!=0:
        guess= (lastguess + x/lastguess)/2
        if abs(guess - lastguess) < .000001: 
            return guess
        lastguess= guess
        
def eud(c,p):
    return sqrt((c[0]-p[0])**2+(c[1]-p[1])**2+(c[2]-p[2])**2)
    

def Center(k):
    centers = {}
    cluster={}
    for i in range(k):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        center=(r,g,b)
        centers[i]=center
        cluster[(r,g,b)]=[]
    return centers , cluster

def clustering(points,k):
    centers,cluster=Center(k)
    dis1,mindis=0,0
    for p in points:
        disdict={}
        for ce in range(len(centers)):
            c=centers[ce]
            disdict[ce]=eud(c,p)
        for i in disdict.keys():
            if disdict[i]==min(disdict.values()):
                dis1+=disdict[i]
                flag1=True
                if dis1<mindis or flag1==True:
                    Flag1=False
                    mindis=dis1
                for j in cluster.keys():
                    if j==centers[i]:
                        cluster[j]+=[(p[0],p[1],p[2])]
    return cluster,centers

def bestcluster(k,cluster,centers):
    newcluster={}
    while newcluster!=cluster:
        mean=[]
        for c in range(k):
            r,g,b=0,0,0
            for p in cluster[centers[c]]:
                r+=p[0]
                g+=p[1]
                b+=p[2]
            n=len(cluster[centers[c]])
            if n==0:
                n=1
            mr=r//n
            mg=g//n
            mb=b//n
            mean+=[(mr,mg,mb)]
        dislist=[]
        for j in range(k):
            dislist+=[[]]
        for c2 in range(k):
            points=cluster[centers[c2]]
            count=-1
            for p2 in points:
                count+=1
                for m2 in mean:
                    dislist[c2][count]=eud(m2,p2)
        for i in dicdist.keys():
            if dicdist[i]==min(dicdist.values()):
                newcluster[centers[i]]=p2
    return newcluster
                                          
