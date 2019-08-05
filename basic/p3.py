'''
연속데이터(시퀀스 타입)
    > 리스트: [] -> js의 배열과 동일, 순서가 존재, 값 중복 ok, 
                   인덱스는 정방향/역방향(-1,-2,...) 존재
'''
# 비어있는 리스트 생성
# 정적 생성 => 일반적으로 문제는 없으나, 간혹 추가가 안되는 경우가 생김
#             이런 경우 동적 생성으로 대체
#             => 자료구조를 직접 맞춰서 데이터를 세팅하는 리스트 내포같은 케이스에 사용
nums = []       
print( nums, len(nums), type(nums) )
# 동적 생성 => 대량의 작업시 조듬 더 안정적
nums = list()   
print( nums, len(nums), type(nums) )
nums = [1,3,5,7,9]
print( nums, len(nums), type(nums) )
anis = [ 'dog', 'cat', 'bird' ]
print( anis, len(anis), type(anis) )
# 리스트의 맴버들의 타입이 다르면 리스트를 구성할 수 있다
# (파이썬은 모든 것이 객체이므로, 맴버들도 모두 객체이다)
# -> 본질적으로는 차이가 없다
# -> 주소를 가지고 있고, 이것이 포함되어 있음
mix = [1,2,3,'dog','cat']
print( mix, len(mix), type(mix) )
# 차원을 섞으면 맴버중에 하나가 리스트였다
multiTypeMatrix = [1,2,3,'dog','cat', ['bird', 100]]
print(multiTypeMatrix, len(multiTypeMatrix), type(multiTypeMatrix))
#############################################################################
# multiTypeMatrix에서 100이란 값을 출력하시오(연속데이터 타입에서 하나만 콕 찝어서 뽑아내라)
# -> 인덱싱 (이라는 것을 유추할 수 있어야 한다)
print( multiTypeMatrix[-1][-1])
#########################################################################
# 슬라이싱 => 사본작업
nums = [1,3,5,7,9]
# nums에서 3,5,7만 가진 리스트를 구하시오 : 리스트 -> 리스트(슬라이싱:차원유지)
print(nums[1:-1], '사본출력' ) 
# 위의 소스코드는 원본은 유지된다. => 원본변경 방법은
nums[0] = 100       # => 인덱싱을 활용한 변경
print( nums )
# 3,5,7을 모두 -1로 변경하시오
# nums[1:-1] = -1     # => error, 
nums[1:-1] = '-1'   # 체급이 같아져서 가능
# 같은 시퀀스(연속데이터) 타입이면 슬라이싱 범위를 대체할 수 있다
print( nums )
#########################################################################
# 맴버삭제(보편적인 방법)
del nums[0]
print( nums )
# 9값을 가진 맴버삭제(하나 콕 찝어서)
nums.remove( 9 )
print( nums )
nums = [1,3,2,3,4,3,5,7]
# 중복된 데이터중 가장 먼저(정방향) 찾은 맴버를 제거
nums.remove( 3 )
print( nums )
# 다제거
nums.clear()
print( nums )
# 빈집에 맴버 추가
nums.append( 1 )
print( nums )
tmp = [3,5]
# 오직 자식으로 추가
nums.append( tmp )
print( nums )
# 리스트를 이어붙였다     => 원본변경
nums.extend( tmp )
print( nums )
# 두개를 이어 붙여서 리턴 => 사본작업
print( nums + tmp )
print( nums )
# 리스트에서는 정적이냐 동적이냐, 순서가 있다, 전처리 레벨에서는 사용될 수 있다, 빅데이터는 무리

# 리스트와 for => for문에서 확인
















