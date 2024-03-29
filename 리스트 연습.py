# 리스트 메소드(함수) 연습

a = ['하나', '둘', '셋', '넷']
print('원본 a =', a)


a.append('다섯')
print('append(\'다섯\') 사용 후 :', a)   # 공백 없이 바로 콤마(,) a 하니까  출력창에 알아서 공백 하나 들어감
print()                            # 또한 print('append() 사용 후 :' + a) 는 에러.  a가 리스트라 문자열하고 + 연산 안됨.


a.insert(0, '제로')  # 리스트.insert(인덱스, 데이터) : 인덱스 위치에 데이터 삽입
print('insert(0, \'제로\') 사용 후 :', a)
print()


a.remove('제로')   # 리스트.remove(데이터) : 해당 데이터가 일치하는 첫 번째 요소 제거. 없으면 에러 발생. 예외처리 추천
print('remove(\'제로\') 사용 후 :', a)
print()


print('a[-1] = {0}\n'.format(a[-1]))  # 인덱스[-1]은 가장 마지막 값을 나타냄


print('a.pop() 사용 전 a =', a)
print('a.pop() = {0}'.format(a.pop()))      # 리스트.pop() : 리스트 마지막 요소를 반환하며 제거
print('a.pop() 사용 후 a =', a)
print()   # 그냥 print() 하면 한 줄 공백 만들 수 있다


b = [1, 2, 3, 4, 5]
print('원본 b =', b)
print('b.pop() = {0}'.format(b.pop()))
print('b.pop() 연산 후 b =', b)
print('b.pop(1) = {0}'.format(b.pop(1)))  # 리스트.pop(인덱스) : 해당 인덱스 위치의 요소를 반환하며 제거
print('b.pop(1) 연산 후 b =', b)
print()


a = ['김씨', '이씨', '박씨', '최씨', '조씨', '김씨']
print('a =', a)
print('a.index(\'이씨\') =', a.index('이씨'))     # 리스트.index(데이터) : 일치하는 첫 번째 요소 인덱스를 알려준다. 없으면 에러 발생.
print('a.index(\'이씨\') = {0}'.format(a.index('조씨')))  # 위 print()문과 같은 다른 방식으로 표현. 그냥 범용적인 .format() 쓰는게 좋을듯
print()


print('a.count(\'김씨\') = {0}'.format(a.count('김씨')))  # 리스트.count(데이터) : 일치하는 요소의 개수를 센다.
print()


b = [2, 3, 1, 5, 9, 4]
print('원본 b =', b)
b.sort()   # 리스트.sort() : 오름차순으로 데이터 정렬
print('b.sort() 사용 후 =', b)
print()


b = [2, 3, 1, 5, 9, 4]
print('원본 b =', b)
b.sort(reverse = True)   # 내림차순으로 데이터 정렬. 반드시 reverse=True 를 입력해야됨. True만 하면 에러.
print('b.sort(reverse = True) 사용 후 =', b)
print()


a = ['안', '녕', '하', '세', '요']
print('원본 a = ', a)
a.reverse()   # 리스트.reverse() : 리스트 내 요소의 순서를 반대로 뒤집는다.
print('a.reverse() 사용 후 = ', a)   # 함수 설명에 (method) def reverse() -> None   여기서  -> None 뜻이 반환값(return 값)이 없다는 거구나..


# 2차원 리스트 연습

print('2차원 리스트 연습')
two_dimention_list = []  # 기본 1차원 리스트 초기화
two_dimention_list.append([])  # append()함수를 써서 

two_dimention_list[0].append(0)
two_dimention_list.append(0)
print(two_dimention_list)
print()


two_dimention_list = []  # TODO: 이렇게 하면 위에 선언 했던 변수가 지워지고 새롭게 정의되는건가? 알아보자
print('n x n 리스트 만들 숫자를 입력하시오 : ', end='')  # 입력 받기 전 end='' 옵션 넣으면 한줄에 이쁘게 입력할 수 있다
n = int(input().strip())  # 입력 받음과 동시에 공백이 있으면 제거.

for i in range(n):
    two_dimention_list.append([])  # ?? 이렇게하면 동적으로 생성되나??
    for j in range(n):
        two_dimention_list[i].append(0)

print('만들어진 리스트 : {0} x {1}, lengh={2}, type={3}'.format(len(two_dimention_list), len(two_dimention_list[0]), len(two_dimention_list), type(two_dimention_list)))
# 아.. 이제야 동적으로 2차원으로 리스트 만드는게 이해가 되네..

for i in range(len(two_dimention_list)):
    for j in range(len(two_dimention_list[i])):
        print('{0}'.format(two_dimention_list[i][j]), end=' ')
    print()
print()