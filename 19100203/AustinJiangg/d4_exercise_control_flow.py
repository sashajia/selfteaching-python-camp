a=1
for i in range(9):
    if i==0:
        print(f'{a}*1={a}')
    if i!=0:
        print(f'{a}*1={a}',end='\t')
    d=2
    for j in range(i):
        e=a*d
        if j<i-1:
            print(f'{a}*{d}={e}',end='\t')
        if j==i-1:
            print(f'{a}*{d}={e}')
        d+=1
    a+=1
    


a=1
while a<10 :
    if a==1:
        print(f'{a}*1={a}')
    if a!=1 and a%2!=0:
        print(f'{a}*1={a}',end='\t')
    d=2
    while d<=a and a%2!=0:
        e=a*d
        if d<a:
            print(f'{a}*{d}={e}',end='\t')
        if d==a:
            print(f'{a}*{d}={e}')
        d+=1
    a+=1
