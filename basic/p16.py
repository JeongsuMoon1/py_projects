# 내장함수
# 파일처리, 파일 덤프
'''
mode options
r : 읽기
w : 쓰기
b : 바이너리 모드
+ : 반대 속성 추가, ex) r+ == rw
a : append(추가) 
'''
# 맥락은 열고 읽고 쓰고 닫는다
# 실행시 f1.txt 에 깨진 문자나옴(깨진게 아님, 깨진것 처럼 보이는것-> 읽기 코드로 확인함 18번 줄)
f = open( 'f1.txt', 'w' )
for n in range(10):
    f.write( '%d 라인 line 12!@\n' % n )
f.close() # 꼭 닫아줘야한다

f = open( 'f1.txt', 'r' )
print( f.read() )
f.close()

# I/O 에서는 열었으면 반드시 닫아야 한다 !!
# 간혹 누락시키는 경우가 존재한다 => 원천적으로 해결하는것이 좋다 => 자동으로 닫히게
# with문 ~:  -> 자동으로 닫히는 기능(?), with문에는 f.close문이 없다
# I/O문에서는 with를 항상 검토한다
with open( 'f1.txt', 'r' ) as f: # with뒤에 open함수 호출되는 형태, f를 별칭을 준다(open은 f다)
    print( f.read() )
#############################################################################################
# 외장함수
# 피클 (pickle) => 자료구조를 유지해서 덤프, 로드
# 머신러닝에서도 피클을 커스터마이즈해서 지원해주고 있다
# 예를들어 파파고 머신러닝의 스킬중의 기초가 되는 것(피클)
import pickle as p
data = {
    1:[1,2,3,4],
    2:{'name':'품질'},
    3:(5,6,7,8)
}
# 덤프
with open( 'data.p', 'wb' ) as f1: # .p :확장자(아무거나 씀)
    p.dump( data, f1, p.HIGHEST_PROTOCOL )
# 로드
with open( 'data.p', 'rb' ) as f2:
    tmp = p.load( f2 )
    print( tmp, type(tmp) ) # f2 찍었을때 34번 줄 호출, -> 실행 결과 data.p 파일에 읽을 수 없다 출력

# OS 모듈 
import os
# 실행 결과 : 현재 프로젝트 경로 출력
print( os.getcwd() ) 
# 제시된(현재) 디렉토리에 존재하는 모든 파일, 디렉토리들을 리스트로 나열해라
print( os.listdir( os.getcwd() ) ) 




























