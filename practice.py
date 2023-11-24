# bool 자료형과 논리연산자 연습
a = True  # Python에서는 bool타입 변수 true, false가 대문자로 시작한다
b = False
c = 1   # int 1, 0으로도 참 거짓이 되는지 확인을 위한 변수
d = 0
print('a = True, b = False')

if (a):   # 논리연산자는 True, False를 반환
    print('if(a) :', a)
if (not b):   # Python에서는 논리연산자 !가 아니라 not을 붙인다
    print('if(not b) :', not b)
print('a and b :', (a and b))  # 논리연산자 and
print('a or b :', (a or b))  # 논리연산자 or
if(c):
    print('if(c) : True,  type:{0}'.format(type(c)))
if(not d):
    print('if(not d) : True,  type:{0}'.format(type(d)))
print()

print(bool([]))   # 때때로 bool(매개변수) 함수는
print(bool([1,2]))  # 해당 리스트가 비어있는지 안 비어있는지 판가름 할 수도 있다
print()


# 입력문 연습
print('수를 입력하세요 : ', end = '')   # end=""을 매개변수로 입력하면 줄바꿈을 출력하지않는다.
e = int(input())  # 입력받은 결과를 정수형으로 변환
print('입력받은 수 : {0}'.format(e))
print()


# 전역 변수(Global Variable) 키워드 global
print('전역 변수 global 키워드 연습')

def global_Func():
    global global_v  # global 키워드로 변수를 지정 후에 사용
    global_v = 3
    print('global_v : {0}'.format(global_v))

global_v = 1  # 새롭게 초기화
global_Func()  # 1로 초기화된 global_v 자체를 함수 내에서 3으로 변경
print('전역 변수 연습 함수 global_Func() : {0}'.format(global_v))
global_v = 1
print('변경 후 전역 변수 {0}'.format(global_v))
print()


# pass 키워드. 함수나 클래스의 구현을 나중으로 미루겠다.
def empty_Func():  # 파이썬처럼 들여쓰기를 이용하는 언어는 '빈 구현'을 만들 때 난감하기 때문에 사용
    pass

