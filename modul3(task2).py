def get_hash(s,x,p):
    hs=0
    for i in range (len(s)):
        hs=(hs*x+ord(s[i]))%p
    return hs

def func(s,t,x,p):
    if s!=t:
        k=1
        t=t[1:]+t[0]
        hs=get_hash(s,x,p)
        ht=get_hash(t,x,p)
        xt=1
        for i in range(len(s)-1):
            xt=(xt*x)%p
        for i in range(len(t)-1):
            if hs==ht:
                break
            else:
                ht=(x*(ht-ord(t[i])*xt)+ord(t[i]))%p
                k+=1
        if hs==ht:
            print(k)
        else:
            print(-1)
    else:
        print (0)

def main():
    s=input() #zabcd
    t=input() #abcdz
    x=26
    p=1*10**9+7
    func(s,t,x,p)

main()
