# 1
def solution(friends, gifts):
    answer = 0

    # 2 <= friends = 친구들의 수 <= 50
    # friends의 원소는 알파벳 소문자로 이루어진 길이가 <= 10 인 문자열 배열
    # 이름이 같은 친구는 없다

    # 1 <= gifts의 길이 <= 10,000
    # gifts의 원소는 "A B" 형태의 문자열이다.
    # A는 선물을 준 친구의 이름, B는 선물을 받은 친구의 이름. 공백 하나로 구분
    # A와 B는 friends의 원소이며 A와 B는 같은 이름이 경우는 존재하지 않는다.

    # if 두 사람이 선물을 주고받은 기록이 있다. (두 사람끼리의 비교)
    # 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받는다.

    # if 두 사람이 선물을 주고받은 기록이 하나도 없거나, 주고받은 수가 같다면 (전체 친구 비교)
    # 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받는다.


    # 각 친구마다의 선물 받은 기록, 준 기록, 선물 지수  관리해야될듯


    index = 0
    index_1 = 0
    test = [[friends[0], 0, 0, 0]]  # [0]:이름, [1]:준 선물, [2]:받은 선물, [3]:선물 지수
    gift_test = []  # gifts 리스트에서 공백 제거한 리스트
    gift_change = []  # ex) [0]:muzi, [1]:ryan, [2]:frodo, [3]:neo 2중 배열    =>  가변 변수로 바꾸자
    next_month_point_seq = []  # 최종 점수. 인덱스는 gift_change와 동일   => 가변 변수로 바꾸자

    index_range = len(friends)
    print('index_range 값 : {0}'.format(index_range))

    # 데이터 초기화
    for i in friends:
        if(index == 0):  # 인덱스 0 : 첫 번째 친구(이미 초기화 데이터로 사용함)
            index += 1
            continue
        test.append([i, 0, 0, 0])  # 친구 이름마다 준 횟수, 받은 횟수 0으로 초기화해서 새로 저장
        #gift_change.append([0, 0, 0, 0]) # 친구 이름마다 서로 교환횟수 비교하기 위해 따로 저장
        index += 1

    

    #for i, j in range(index_range):
    #    gift_change.insert((i, j), 0)
    for i in range(index_range):
        gift_change.append([])  # ?? 이렇게하면 동적으로 생성되나??
        next_month_point_seq.append(0)  # 인원 수 만큼 동적으로 생성.
        for j in range(index_range):
            gift_change[i].append(0)

    print('gift_change : length={0}, type={1}'.format(len(gift_change), type(gift_change)))
    for i in range(len(gift_change)):
        for j in range(len(gift_change[i])):
            print('{0}'.format(gift_change[i][j]), end=' ')
        print()

    print('next_month_point_seq : {0}'.format(next_month_point_seq))

    for i in range(len(test)):
        print('test : {0}, {1}, {2}, {3}'.format(test[i][0], test[i][1], test[i][2], test[i][3]))
    
    print('gift_change : ', end='')
    for i in range(len(gift_change)):
        for j in range(len(gift_change[i])):
            print('{0}'.format(gift_change[i][j]), end=' ')
        print()


    # gifts 데이터 분리해서 따로 gift_test 리스트에 저장
    for i in range(len(gifts)):
        gift_test.append(gifts[i].split(' ')) # 공백을 기준으로 나눠서 리스트로 만든다
        print('gift_test : {0}, {1}'.format(gift_test[i][0], gift_test[i][1]))


    # 준 선물, 받은 선물 개수를 각각 test 리스트의 이름에 대입
    for index in range(len(test)):
        for i, j in gift_test:
            if(test[index][0] == i):
                test[index][1] += 1
            elif(test[index][0] == j):
                test[index][2] += 1
    

    # 선물 지수 계산
    for i in range(len(test)):
        test[i][3] = test[i][1] - test[i][2]

    for i in range(len(test)):
        print('{0}, {1}, {2}, {3}'.format(test[i][0], test[i][1], test[i][2], test[i][3]))


    # 누가 누구에게 주고 받았는지 배열 만들기
    for i in range(len(friends)):   # n x n 행렬
        for j, k in gift_test:    # 각자 이름을 비교하며 해당 인덱스일 때의
            if(friends[i] == j):   # gift_change[][] 값을 +1 해준다
                for index_1 in range(len(friends)):
                    print('index={0}'.format(index_1))
                    if(friends[index_1] == k):
                        gift_change[i][index_1] += 1
                        print('[{0}][{1}]'.format(i, index_1))
                    #index_1 = 0


    print('[주고 받은 횟수 테이블]')
    for i in range(len(gift_change)):
        for j in range(len(gift_change)):
            print('{0}'.format(gift_change[i][j]), end=' ')
        print()

    for i in range(len(gift_change)):
        for j in range(len(gift_change)):
            if(i == j):  # 같은 이름인 칸은 -1로 초기화
                gift_change[i][j] = -1
            else:  # 본인끼리 비교 제외
                if(gift_change[i][j] != 0):  # 두 사람이 선물을 주고받은 기록이 있을 때
                    if(gift_change[i][j] > gift_change[j][i]): # 서로 비교하며 큰 쪽에 값을 +1 해준다
                        next_month_point_seq[i] += 1

                elif((gift_change[i][j] == 0 and gift_change[j][i] == 0) or (gift_change[i][j] == gift_change[j][i])):  # 두 사람이 선물을 주고받은 기록이 없거나, 주고받은 수가 같다면
                    if(test[i][3] > test[j][3]):  # 선물 지수 값을 비교한다
                        next_month_point_seq[i] += 1  # 지수가 더 큰쪽에 +1 해준다
                    elif(test[i][3] == test[j][3]):  # 선물 지수도 같을 때
                        next_month_point_seq[i] = next_month_point_seq[i]+0  # 생략해도되나?

    #for i in range(len(next_month_point_seq)):
    #    next_month_point_seq[i] = next_month_point_seq[i] / 2  # for문을 다 돌면 2번씩 계산된걸 감안해  값/2를 해준다

    
    print('개개인의 다음 달에 받게 될 선물 수')
    for i in range(len(next_month_point_seq)):
        print('{0}'.format(next_month_point_seq[i]), end=' ')
    print()
    print()

    answer = max(next_month_point_seq)
    
    return answer



solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])

solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])

solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"])
