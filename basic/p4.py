'''
> 딕셔너리: {} -> js의 객체와 동일, 순서x, 키:값, 키는 중복되면 안된다,
                 값은 중복되도 된다
                 => 테이블상의 한개의 row, json의 객체와 동일
'''
# 이 스타일(첫번째 소스코드)을 가장 많이 사용
dic = {}
print( dic, len(dic), type(dic) )
dic = dict()
print( dic, len(dic), type(dic) )
#####################################################
# 키를 통해서 값을 이해할 수 있다. 직관적으로
dic = {
    'name':'홍길동',
    'age':100
}
print( dic, len(dic), type(dic) )
# 인덱싱 : 순서가 없으므로, 데이터를 특정할 수 있는 키값을 특정하여 사용한다
print( dic['name'] )
# 데이터추가, 카는 뭐든지 올 수 있다. 2는 인덱스가 아닌, 키를 의미
dic[2] = 'hello'
print( dic, len(dic), type(dic) )
print( dic[2] ) # 키가 2인 인덱스를 찍어라
######################################################################
print( dic.keys() )   # 키들이 리스트로 나온다
print( dic.values() ) # 인덱스 값들이 나온다
# 키 조사
print( 'name' in dic)  # dic안에 name이 존재하는가?
# for문으로 돌려보기 => for에서 확인



























































































































