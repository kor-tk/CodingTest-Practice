# 문자열, 문자열 함수(메소드), print문, input()문 연습

a = 'Hello My name is {0}, {1} years old'.format('K', 77)
print(a)
b = 'Hello My Job is {Job}, I\'ve been working for {num} years!'.format(Job='Teacher', num=7)  # \(역슬래시)붙이면 문자로 인식함.
                                                                        # 변수를 만들어 넣어도 됨
print(b)
print()



c = 'Apple,Orange,Kiwi'
d = c.split(',')  # 문자열 분리 함수 split(매개변수)
print(c)   # 원본 문자열 변화 없음
print(d)   # ',' 기준으로 문자열 나뉨
print()



print('문자나 숫자를 입력하세요 : ')
e = input()   # input() 함수는 입력함수. 전달하는 데이터의 형식이 문자열이다.
if(e.isalpha()):
    print('문자입니다. {0}'.format(e))
    print(type(e))  # type=str
elif(e.isnumeric()):
    print('숫자입니다. {0}'.format(e))
    print(type(e))  # type=str
print()




print('첫 번째 숫자를 입력하시오 : ')
a = input()
print('두 번째 숫자를 입력하시오 : ')
b = input()
c = int(a) * int(b)    # 형변환을 해줘서 str->int로 변환 후 계산 가능
print('{0} * {1} = {2}'.format(a, b, c))
print(type(c))   # type=int
print()




d = int(a) * b  # int를 한쪽에만 주면.. 문자열b가 a번 반복된다
print('한쪽만 형변환 후 계산.  int({0}) * {1} = {2}'.format(int(a), b, d))
print()


a = '안녕하세요'
print('a =', a)
print('a[3] = {0}'.format(a[3]))
# a[3] = '2'     # 이와같이 문자열 자체를 변경하는 건 불가능하다. 오류 발생
# print('a =', a)
