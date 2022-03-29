a,b=map(int,input().split())
t=2
hcf=1
while True:
    if a%t==0 and b%t==0:
        a=a//t
        b=b//t
        hcf=hcf*t
    else:
        t+=1
    if a<t or b<t:
        break
print(hcf)