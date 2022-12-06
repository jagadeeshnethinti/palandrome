a=int(input())
rev=0
rem=0
r=a
while(a!=0):
    rem=a%10
    rev=rev*10+rem
    a=a//10
if rev==r:
    print('palandrome')
else:
    print('not a plandrome')
    