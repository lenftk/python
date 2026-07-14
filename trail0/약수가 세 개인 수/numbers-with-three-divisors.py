start, end = map(int, input().split())

ans=0
# Please write your code here.
for i in range(start,end+1):
    cnt_prime=0
    for j in range(1,end+1):
        if i%j==0:
            cnt_prime+=1
    if cnt_prime==3:
        ans+=1
print(ans)