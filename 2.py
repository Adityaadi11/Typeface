s1=input()
s2=input()
lastChar=s2[-1]
count=0
for i in s1:
    if i==lastChar:
        count+=1
print(count)