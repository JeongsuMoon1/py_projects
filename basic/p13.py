# class
# 파이썬에서 자기 자신 객체를 가르키는 키워드는 self 이다
# self => python, objective-c
# this => java, js, 대다수 랭귀지
class Person:
    '''
    맴버 변수 
    '''    
    name   = None   # 맴버 변수들 정의할 때에는 항상 초기값 작성해준다
    age    = 0
    weight = 0
    '''
    맴버 함수
    '''
    def eat( self, food ):
        print( '%s를 먹는다' % food )
    '''
    생성자 -> 객체를 생성하고, 맴버변수를 초기화 하는데 목적이 있다
    '''
    # repr : 자라로 치면 toString -> 설명하는 것
    def __init__(self, name, age, weight):
        # 클래스 내부에서 맴버들을 접근할때, self.맴버(변수/함수)
        self.name = name
        self.age = age
        self.weight = weight
        # 부모 생성자 호출
        # return super().__init__()

    '''
    객체를 설명하는 코드를 구현된다. 통상 문자열로 구성
    맴버 변수값이나 상태를 표현한 정보가 들어가면 ok
    자바의 toString()의 맥락과 유사하다
    '''    
    def __repr__(self):
        return '''
            name=%s age=%s weight=%s
        ''' % (self.name, self.age, self.weight)
# 객체 생성
obj = Person( '품질', 1, 2)
print( obj )
obj.eat('1')









    




    
    
    
    
    
    
