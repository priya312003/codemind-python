n,m=map(int,input().split())
if n==m+1 or m==n+1:
    print('Yes')
elif n==1 and m==10:
    print('Yes')
elif m==1 and n==10:
    print('Yes')
else:
    print('No')