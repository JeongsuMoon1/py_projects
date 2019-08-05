# 단일데이터 (단일 타입)
# 문자열(연속이지만, 이쪽으로도 분류한다)
# 표기법
# ' ... ', " ... ", ''' ... ''', """ ..."""
# ''' ... ''', """ ...""" 용도 : 여러줄 표현, 구조유지, 여러줄 주석용 
a = 'hi'
print( a )
a = "hi"
print( a )
# 혼용 표현
a = 'abcd"kkk"egf'
print( a )
# 이스케이프 문자로 동일 기호를 내부에서 사용 가능: \
a = 'abcd\'kkk\'egf'
print( a )
# 여러줄
a = '''
fasdfasd
fasdf
asdf
asd
f
'''
print( a )
"""
여러줄 주석
"""
###########################################
# 문자열 더하기 (이어붙이기) <-> 문자열안에 문자열(포멧팅)
a = 'hello'
b = 'lunch'
print( a + b )
# 문자열 반복
print( '1'*10 )
#########################################################################
# 인덱싱 : indexing : 문자열에서 특정 문자를 획득하는 방식(문자열에서 문자를)
# -> 차원축소(인덱싱은 차원축소라는 의미)
# 문법 : 변수명[ 인덱스(정방향 or 역방향 <= 선택기준 : 가까운쪽이) ]
a = '0123456789'
# 2를 출력하시오
print( a[2] )
print( a[-8], '뒤에서 체크하면 머니까 가까운쪽에서 해결한다' )
##########################################################################
# 슬라이싱 : 데이터에서 범위에 해당되는 데이터를 획득
# -> 차원유지 : 2차원에서 인덱싱하면 1차원
# 문법 : 변수[시작인덱스:끝인덱스:step(짜르는 간격, 생략하면 1)] -> 풀문법
# a를 카피한다
print( a[:] ) # step 생략하는 것은 간격이 그냥 1이라는 뜻
# 1~8 까지 출력하시오
# 뒤에 경계값을 포함 안됨
print( a[-1], a[1] )
# a<= <b
print( a[1:-1] )
print( a[1:-1:2] )
###########################################################################
url = 'https://www.pexels.com/photo/beautiful-beauty-blue-bright-414612/image.png'
# 위의 이런 문자열의 파일명 추출, 도메인 추출 등등 사용가능(정제한다)
print( a[:2], a[-2:] )
#########################################################################
# 맴버함수(문자열)
#''. 별4개함수 나옴
a = "0123456789"
# 문자열내에 특정 문자 개수
print( 'a라는 문자열의 2의 개수', a.count('2') )
print( 'a라는 문자열의 A의 개수', a.count('A') ) # 없으면 출력값 : 0
# a라는 문자열에 "A"라는 문자가 존재하는가?
print( a.count('A') > 0 )
print( a.index('2') )
# 에러, 없는 문자는 예외처리 해야한다
#print( a.index('A') )
print( a.find('2') )
print( a.find('A') )
# 문자열에서 문자열 찾기는 count(), find()를 사용해라
#########################################################################
b = ','
# 조인
print( b.join(a) )
# 분해
print( b.join(a).split(b) )
# 공백제거
a = '   sdffs sdfef fsdf    '
print( '[%s]' %a.lstrip() )
print( '[%s]' %a.rstrip() )
print( '[%s]' %a.strip() )
# 가운데 공백 제거 => 정규식
# 대소문자
a = 'abcdABCD가나다라1234!@#$'
print( a.upper() )
print( a.lower() )
# 조합사용
url = 'https://www.pexels.com/photo/beautiful-beauty-blue-bright-414612/image.png'
# => image.png 라는 문자열을 획득하시오, 리스트 인덱싱 정도 사용
# 단, 상수값을 쓰지 않는다.
# print( url[-9:] )
# 1번 방법 : 상수값이 들어가는 방법
print( url.split('/') )     # 쪼개고 리스트화 시킨다
print( url.split('/')[-1] ) # -1은 리스트 맨뒤에 것
# 2번 방법 : 정규화시킨다(일반화시킴)
tmp = url.split('/')
print( tmp )
print( len( tmp ) )
print( url.count('/') )
print( tmp[-1] )
print( tmp[len(tmp)-1] )
print( url.split('/')[url.count('/') ] )
#########################################################################
# 포맷팅
a = 1
b = 2
# x + y = z 형식으로 출력하시오
#print( 'x + y = z' % (a, b, a+b) ) # % ()의 괄호는 튜플
print( '%d + %d = %d' % (a, b, a+b) )
# %s로 받는 경우 => 데이터가 문자열일때 , 데이터의 타입을 모를때
print( '%s + %s = %s' % (a, b, a+b) )
print( '%d + %d = %f' % (a, b, a/b) )
print( '%d + %d = %s' % (a, b, a/b) )

# .format() 처리
# print( ''.format() )
print( '{} + {} = {}'.format(a, b, a+b) )
print( '{0} + {1} = {2}'.format(a, b, a+b) )
print( '{1} + {0} = {2}'.format(a, b, a+b) )
# format의 파라미터를 모두 다 쓸 필요는 없다 -> 그런데 굳이
print( '{1} + {1} = {1}'.format(a, b, a+b) )
print( '{0} + {1} = {result}'.format(a, b, result=a+b) )
# error , 파라미터는 지역변수(함수안에서만 존재함)
#print( result )

#포멧팅, 자리수 체크
print( '[%s]' % '12345' )
# 20칸에 배치
print( '[%20s]' % '12345' )     # 뒤쪽 정렬
print( '[%-20s]' % '12345' )    # 앞쪽 정렬
print( '[%0.2f]' % 3.1456789 )  # 소수점 2째자리 반올림 받음 -> 수치가 바뀐다
print( '[%0.2f]' % 3.1446789 )  # 반올림 받지 않음 -> 수치 안바뀜
print( '[%10.2f]' % 3.1446789 ) # 전체 데이터가 10칸
print( '[%10s]' % '12345' )     # 뒤쪽 정렬
# 치환식 
a = 'abc{}egf'.format('k')
print(a)
# 자리수 10개,
a = 'abc{0:<10}egf'.format('k')
print(a)
a = 'abc{0:>10}egf'.format('k')
print(a)
# 짝수칸일 경우 앞쪽으로 센터 위치
a = 'abc{0:^10}egf'.format('k')
print(a)
# *로 빈칸채우기
a = 'abc{0:*^10}egf'.format('k')
print(a)

















