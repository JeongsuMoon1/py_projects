import pymysql



# 웹에서 pymysql.github에서 example 소스 코드 복사해서 가지고 올 것
# -> 접속문을 try문으로 집어 넣어라



# 데이터베이스 접속은 I/O이므로 예외 상황이 항시 발생할 수 있다 -> try~
connection = None
try:

    # 1. 데이터베이스 접속 개체 생성 => 접속 정보 제공 => 접속
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 db='python_db',
                                 charset='utf8mb4')
    # 2. 커서를 획득한다
    # <기본 문형>..with문은 제외된다 
    #cursor = connection.cursor()
    #...
    #cursor.close()

    # <함축 문형>
    with connection.cursor() as cursor:# Read a single record
        # 3. 쿼리를 수행한다
        sql = '''
        select src, slang as label from tbl_trans_log;
        '''
        # 쿼리 수행시 데이터를 넣고 싶다면 튜플로 2번인자에 채운다
        cursor.execute(sql)
        # 4. 결과 획득(select) 혹은 커밋(insert, update, delete)
        # fetchall()은 다 가져온다, fetchone()은 한개만 가져온다(로그인)
        result = cursor.fetchall()
        # 현재구조는 튜플에 튜플로 나온다 ( (), (), () )
        # 여러가지 경험상 리스트에 튜플이 가장 적합 -> 원하는 것 : [ {}, {}, {} ]
        print(result)

    

except Exception as e:
    print('오류 발생', e) #개발과정에서 오류 발생할 수 있으니 문자열 하나 끼워둘거 
finally:
    # 4. 접속닫기)
    if connection:
        connection.close()