i = 1
d_sum = 0
s_sum = 0
while i <= 100:
    if i%2 == 0:
        d_sum += i
    else:
        s_sum += i
    i += 1
print("偶数%d和"%d_sum)
print("奇数%d和"%s_sum)
