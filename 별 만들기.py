# 별 만들기




while(1):
    print('반복횟수를 입력하시오 : ', end="")
    count = input().strip()    # 입력을 받고, 공백을 없앤다.

    if(count.isdecimal()):  # 숫자가 아닌 입력 예외처리
        count = int(count)  # isnumeic(), isdigit(), isdecimal() 등이 있지만
    else:                   # isdecimal()이 평소에 입력받는 0이상 정수만 True값을 반환하기에
        print('잘못된 입력입니다. 0보다 큰 정수를 입력하세요.') # isdecimal()로 걸러내는게 나을듯
        continue

    if(count > 0):
        break
# 기본 별 출력(좌측 기준)
print('기본 별 출력(좌측 기준)')

for i in range(1, count+1):
    for j in range(i):
        print('*', end='')
    print()

print()


# 기본 별 거꾸로 출력(좌측 기준)
print('기본 별 거꾸로 출력(좌측 기준)')
for i in range(count, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

print()


# 기본 별 출력(우측 기준)
print('기본 별 출력(우측 기준)')
for i in range(1, count+1):
    for k in range(count-i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()
print()

