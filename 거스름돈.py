a = "Hello, World, World, Hey~ World"
print(a + "hi+{0}".format(40) + "hi{0}".format(50))


coin = [500, 100, 50, 10]
n = 1260
count = 0
i=1
for i in coin:
    count = n // coin[i]
    n = n % coin[i]

print("최소 거스름돈 개수 : " + count)

