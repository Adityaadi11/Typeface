n=int(input())
dic={0:0,1:1,2:2,5:5,6:9,8:8,9:6}
ans=0
i=1
c=0
def valid(s):
    s1=str(s)
    for i,v in enumerate(s1):
        if int(v) not in dic:
            return False
    return True

while(c!=n):

    if i in dic:
        ans=i
        c+=1
    else:
        s1=valid(i)
        if s1:
            ans=i
            c+=1
    i += 1
print(ans)

