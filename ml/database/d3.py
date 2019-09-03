import pymysql




connection = None
try:

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 db='python_db',
                                 charset='utf8mb4',
                                 # 접속할 때부터 커서의 타입을 딕셔너리형으로 지정해서 넘긴다
                                 cursorclass=pymysql.cursors.DictCursor)
    # 밑의 소스코드 타입 지정방식은 : 매번 커서를 획득할때마다 타입을 지정하는 방식(비효율), 각기 다르게 적용할때 기능
    #with connection.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
    with connection.cursor() as cursor:
 
        sql = '''
        select src, slang as label from tbl_trans_log;
        '''

        cursor.execute(sql)

        result = cursor.fetchall()

        print(result)

    

except Exception as e:
    print('오류 발생', e) 
finally:
    if connection:
        connection.close()