cnt_t = 0
cnt_f = 0
for i in range(10):
    n = int(input())
    if n%3==0:
        cnt_t += 1
    if n%5==0:
        cnt_f += 1
print(f"{cnt_t} {cnt_f}")