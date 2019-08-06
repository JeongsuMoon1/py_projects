# 함수
# function, method
# 반복작업 해소, 재활용성 높이고, 구조적 설계 => 개발시간 단축
'''
def 함수명( [인자명, 인자명, ...] ):  # []는 생략가능함
    statement
    [ return 값 ]
'''
# 함수 정의
def add(x, y):
    return x+y
# 함수 사용
d = add(1, 2)
print( d )

# 가변인자, 함수의 입력의 수가 가변
def add2( *args ):
    print( args )
    # 인자로 전달된 데이터를 모두 더해서(누적합) 리턴하시오
    sum = 0
    for arg in args:   # for문의 장점: 갯수에 상관없이 한놈씩 끄집어내서 수행한다(그래서 반복문임)
        sum += arg
    return sum

print(add2(1,2))
print(add2(1,2,3))

# 가변인자로 전달된 데이터의 누적합과 누적곱을 계산하여 리턴하시오
def mix( *args ):
    sum, mul = ( 0, 1 ) # 한줄로 표현시 튜플로 표현
    for arg in args:   
        sum += arg
        mul *= arg
    # 리턴할 값이 여러개면 튜플로 리턴된다
    return sum, mul 

print(mix(1,2))
print(mix(1,2,3))
# 서로 관계없는 것들을 묶어서 값을 하나로 나타내는 것 -> 튜플로 온다( 튜플은 순서가 중요하다 )
# 데이터를 받을 때 반드시 순서를 확인해야한다 -> 순서 상관하고 싶지 않으면 딕셔너리를 쓴다
a, b = mix(1,2,3,4,5,6)
print( a )
print( b )

# 리턴을 딕셔너리로 해보자 => 출력 결과에 대해서 순서를 몰라도 된다. 키만 알면 된다
def mix2( *args ):
    sum, mul = ( 0, 1 ) 
    for arg in args:   
        sum += arg
        mul *= arg
    return { "sum":sum, "mul":mul }  # 리턴이 딕셔너리라는 뜻이다.
print( mix2(1,2,3,4,5,6)['mul'] )

# 로그함수
# env_debug = True
# env_debug = False -> 프로젝트 끝나면 False시킨다, ( 교과에는 없는 스킬.현장에서 쓰임)
env_debug = True
def log( msg ):
    if env_debug:
        print('-'*50)
        print( msg )
        print('-'*50)
log( '이것은 로그 메시지 출력 함수이다' )

# 사용자 정의 함수 : 형태를 정의할 수 없다. 만드는 사람 마음이니까 => 프로젝트시 네이밍에 대한 정의가 필요하다
# ex) kbs_ml_analysis_ : 임의로 만든 함수에 대한 설명을 _구분짓는다
# 내장함수 : len(), type(), int(), str(), tuple(), dict(), list(), ...
# 외장함수 : random.randint(), sys.exit()    

# 함수 인자에 대한 초기값 주기
# 초기값 인자들이 존재하면, 초기값 인자는 앞으로 와야한다
# def setPerson( name='품질', age=20, weight=50, score ): # score를 제외한 나머지 인자만 초기값 준 상태
def setPerson( score, name='품질', age=20, weight=50):
    log( '%s %s %s %s' % (name, age, weight, score) )    

setPerson( 100 )
setPerson( score=55 )
# 기본값이 없는 함수의 파라미터는 반드시 값을 구현해야한다
# error
# setPerson( name='모라' )
# 그냥 나열하면 순서대로 인자로 전달된다
setPerson( 1,2,3,4 )
# 기본값이 부여된 파라미터들은 함수 호출시 순서에 상관없이 명시적으로 사용가능
setPerson( 1, age=1004, name='모라')

log( msg='가나다라' )
log( '가나다라' )




