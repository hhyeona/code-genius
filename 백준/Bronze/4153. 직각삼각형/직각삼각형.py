while True:
    num = list(map(int,input().split()))
    if sum(num) == 0:
        break
    max_num = max(num)
    num.remove(max_num) # 가장 큰 숫자 뺌.
    if (num[0]**2 + num[1]**2) == max_num**2:
        print('right')
    else:
        print('wrong')