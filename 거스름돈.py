coin = [500, 100, 50, 10]
n = 1260
count = 0

for i in range(len(coin)):
    count = count + n // coin[i]   # count += n // coin[i]
    n = n % coin[i]   # n %= coin[i]

print("최소 거스름돈 개수 : {0}".format(count))
