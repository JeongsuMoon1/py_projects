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

#    with connection.cursor() as cursor:# Create a new record
#        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
#
#    connection.commit()
#
#    with connection.cursor() as cursor:# Read a single record
#        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#        cursor.execute(sql, ('webmaster@python.org',))
#        result = cursor.fetchone()
#        print(result)
except Exception as e:
    print('오류 발생', e) #개발과정에서 오류 발생할 수 있으니 문자열 하나 끼워둘거 
finally:
    # 2. 접속닫기)
    if connection:
        connection.close()