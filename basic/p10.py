# 반복문 => for문
a = [1,2,3,4,5]
b = {
    'name':'품질',
    'addr':'모라'
}
c = (1,3,5,7,9)
# for ~ each 스타일만 지원
for item in a: # pass는 대게 한줄 코드면 바로 옆에 붙인다
    # 리스트를 for문으로 돌리면 맴버를 하나씩 꺼낸다
    print( item )
for item in c:
    # 튜플도 상동하다
    print( item )
for key in b: 
    # 딕셔너리
    print( key, b[key] ) # 인덱싱 문법 사용
d = [(1,2),(3,4),(5,6)]
for item in d:
    print( item )
# 튜플은 변수로 받을 때 맴버수와 동수로 변수를 나열하면 순서대로 들어간다
for i,j in d:
    print( i,j )
# 딕셔너리에서 만약 인덱스를 뽑고 싶다면
for idx, key in enumerate(b): # enumerate : 내장함수
    print(idx, key)
# 연속수 만드는 내장함수 => range()
# 0 <= n < 3: 경계값
for n in range(3):
    print(n)    
# 1:시작값 <= n < 4: 경계값
for n in range(1,4):
    print(n) 
# 1:시작값 <= n < 11: 경계값, 간격은 2단위 1->3->5    
for n in range(1,11,2): # 2: step이다(생략하면 간격 1로 준다)
    print(n)

# 3~7 단 구구단 구현
# 형식 : 3 x 1 = 3, 곱의 결과의 자리수는 최대 2자리이다, 1자리 값일때 좌측정렬로 표현
for i in range(3,8):   
    for j in range(1,10):   
        print( '{0} x {1} = {2:>2}'.format(i,j,i*j) )

# 만약에 이런 결과물을 리스트로 담고 싶다면
results = list()
for i in range(3,8):   
    for j in range(1,10):
        # list에 생성된 문자열을 맴버로 추가   
        results.append( '{0} x {1} = {2:>2}'.format(i,j,i*j) )
print( results )
# 한줄로 줄이면 => 리스트 내포, 딕셔너리 내포, 시퀀스 타입은 다 가능하다
# list : []
# 작성법 => 결론의 형태부터 완성 => 각 변수를 기술하면 된다 => 조건이 있으면 추가
# 데이터 수집 및 전처리에서 사용된다 -> db에 통으로 집어넣는 기능을 한다
results2 = [ '{0} x {1} = {2:>2}'.format(i,j,i*j) 
            for i in range(3,8) 
            for j in range(1,10) ] 
print( results2 )




