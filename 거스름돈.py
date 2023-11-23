coin = [500, 100, 50, 10]
n = 1260
count = 0

for i in range(len(coin)):
    count = count + n // coin[i]   # count += n // coin[i]
    n = n % coin[i]   # n %= coin[i]

'''  # 이 방법으로도 된다
for i in coin:
    count += n // coin
    n %= coin
'''
print("최소 거스름돈 개수 : {0}".format(count))
