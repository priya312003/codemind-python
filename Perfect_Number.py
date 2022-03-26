a=int(input())
num=1
sum=0
for i in range(1,a):
    if a%num!=0:
        num+=1
        continue
    sum=sum+num
    num+=1
if (sum==a):
    print('True')
else:
    print('False')
