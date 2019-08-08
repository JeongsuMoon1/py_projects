# 연구목표: 주요포털을 통한 뉴스 해드라인 수집 + 언론사명 + 기자명
# 이를 통해 아베에 대한 언론의 긍정/부정에 대한 뉘앙스 분석
################################################################

import urllib.request
import os
import sys
import json

# 네이터 쿼리 인증키 : 일일 쿼터 25,000 ( 아이디가 많으면 검색할 수 있느 횟수 증가 )
Client_ID = '_kYGPWLxEKgbDV0v7Kn3'
Secret    = 'FNDu62I5Md'

# API URL
news_url = 'https://openapi.naver.com/v1/search/news.json'
# 검색키워드를 고정할 것인가? 디비에서 관리해서 가져올 것인가? -> 우린 디비에서 가져오겠다(향후 -> 필요한것들: 마리아 디비, 테이블, 키워드 및 sql과 거기에 따른 코드가 필요함)
keyword    = urllib.parse.quote('아베')


# url 생성(최종 url)
# 함수로 만들기(코드의 함수화)
def makeFullUrlByGet( news_url, start, size ): # len 집어넣고 바꾸기
    news_param = 'query=%s&display=%s&start=%s&sort=%s' % (keyword, size, start, 'date') # start가 계속 업뎃됨
    url = '%s?%s' % (news_url, news_param)  # %s?%s: get 방식
    return url

# 통신이 필요하다 ( 이건 1페이지만 가지고 오는것(풀코드로 한번은 작성해줘야한다))
# 통신 : 최초 1회 전체 데이터를 다 가져온다 => 1~1000가능, 통신을 한다는 행위 자체가 계속 반복한다는 뜻
# 테스트할 때 전체 크기가 커버리면 결과를 확인하는데 너무 오래 걸린다,
# 임의로 5를 부여하여 4번 정도 확인해 본다(샘플링)
#for start in range(1,5): # 1001): for문이 돌때마다 주소를 만들고 통신을 한다
#    print( makeFullUrlByGet( news_url, start ) )  # -> 여기까지 구동하면 start 1,2,3,4 가 나오는거 확인
#    # 통신 객체 생성
#    request = urllib.request.Request( makeFullUrlByGet( news_url, start ) ) # 이 함수는 1페이지 고정이다, 27번줄로 for문 작성 
#    # 헤더 설정
#    request.add_header("X-Naver-Client-Id", Client_ID)
#   request.add_header("X-Naver-Client-Secret", Secret)
#   # 실제 통신
#    response = urllib.request.urlopen(request)
#    # 결과처리 
#    if(response.getcode() == 200): # 통신성공,  바로 처리하게끔 코드 수정. 
#        tmp = json.load(response) # tmp로 데이터를 받는다
#        # print( [ item['title'] for item in tmp['items'] ] )

# 100개씩 데이터 계속 들어오게 할 것( 
import time
def connectNetwork( sIdx, eIdx, size=100 ): # size 집어넣어주기, 쿼리한번 치면 100개씩 들어온다
    for start in range(sIdx, eIdx): # 1001): for문이 돌때마다 주소를 만들고 통신을 한다
        time.sleep(1*0.4)
        print( makeFullUrlByGet( news_url, start, size ) )  # -> 여기까지 구동하면 start 1,2,3,4 가 나오는거 확인
        # 통신 객체 생성
        request = urllib.request.Request( makeFullUrlByGet( news_url, start, size ) ) # 이 함수는 1페이지 고정이다, 27번줄로 for문 작성 
        # 헤더 설정
        request.add_header("X-Naver-Client-Id", Client_ID)
        request.add_header("X-Naver-Client-Secret", Secret)
        # 실제 통신
        response = urllib.request.urlopen(request)
        # 결과처리 
        
        if(response.getcode() == 200): # 통신성공,  바로 처리하게끔 코드 수정. 
            tmp = json.load(response) # tmp로 데이터를 받는다
            # 디비에 지금 수집한 데이터 100개를 밀어 넣어라
            insertData( tmp['items'] )  # 동기식 : 얘가 끝날떄까지 대기.
            # print( [ item['title'] for item in tmp['items'] ] )

import pandas as pd
import pymysql
from sqlalchemy import create_engine
import pandas.io.sql as pSql # 디비에 실제로 밀어넣는 용도           
def insertData( data ):
        # 연결
        db_url = 'mysql+pymysql://root:1234@localhost/python_db'
        db_url
        # 엔진생성(절차)
        engine = create_engine( db_url, encoding='utf8')
        # 실연결
        conn = engine.connect()
        # 삽입
        df_dict = pd.DataFrame.from_dict( data )
        print( df_dict.iloc[0]['title'] )
        df_dict.to_sql( name = 'tbl_navernews', con = conn, if_exists='append', index = False ) 
        # 해제
        conn.close()
        # 로고
        print( '%d개의 데이터가 입력되었습니다.'% len(data) )


# 이 프로그램의 entry point(시작점, 진입로)
# 여기서부터 프로그램이 시작한다
def main():
    # 최초에는 데이터가 없어서 api가 허용하는 범위내에서 최대치로 데이터를 수집
    # connectNetwork(1, 1000)  마리아 디비에 넣어두고 주석처리 실시 -> size를 100으로 줘서 1000이 아닌 100개가 들어온다
    # 10분 간격으로 데이터를 수집 -> 스케쥴은 os단에서 해결
    # 만약, 새로 수집한 데이터가 디비에 이미 존재한다면? 
    # , 2가지 관점이 있다(중복제거해줘야함)
    # 1번관점 : 입력시 중복체크를 할것인가? 
    # 2번관점 : 그냥 디비에 다 넣어두고 분석할때 중복을 제거할것인가?
    # 지금은, 그냥 밀어넣을것이다.
    connectNetwork( 1, 2, 10 ) # 10개

if __name__ == '__main__':
    main()












