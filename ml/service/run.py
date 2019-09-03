# 엔트리 포인트 -> (중요한 이유) 여기서부터 경로를 따진다.
# 1. 모듈 가져오기
from  flask import Flask, render_template, request, jsonify, redirect # 클래스가 나온다(대문자로)
from ml import detect_lang # __init__를 끌고온다, ml(패키지)를 들고온다
from db import insertData
import urllib.request
import json
import sys
import os

# 2. flask 객체 생성
app = Flask(__name__)

# 3. 라우팅
# ~/ 요청하면 home() 함수가 응답(return)
@app.route('/') # 응답하는 코드
def home():
    return redirect('/kfqgo')

# restful api
# 기본 라우트는 get방식만 허용(오류나는 이유)
@app.route('/kfqgo', methods=['GET','POST']) 
def kfqgo():
    if request.method == 'GET': # request 객체는 1번 모듈에서 땡겨야 사용할 수 있다.(get을 request 요청하는 조건문)
        # 기본으로 templates 폴더 밑에서 찾는다 
        return render_template('index.html')
    else:
        # 여기는 post방식으로 데이터가 요청되었을 때 처리
        # 서비스     : 데이터를 획득 -> 백터화 -> 모델을 로드(서버가동시 1회만) 
        #              -> 답안을 획득 -> 응답 구성
        # 데이터 획득 (모든 데이터는 요청객체를 받고 들어온다(request))
        #a = request.form['inputLang'] # 딕셔너리 구조임 # flask에서 post 방식
       
        check_text = request.form.get('inputLang') # 키가 틀려도 None으로 처리, 별개로 a번 죽이고 check_text번으로 사용한다
        nation, lang_ko = detect_lang( check_text ) #판정
        # 번역 요청
        transText = lang_transByPapago( check_text, nation )
        if transText: # 번역이 되었다면 !!
            transText = transText['message']['result']['translatedText']
        else:
            transText = '번역실패'

        # 1. 파파고 번역으로 연동(통신)
        # 2. 응답 -> 로그 처리(디비 저장) -> AJAX응답
        insertData( src=check_text, 
                    out=transText, 
                    slang=nation, 
                    olang='ko' 
                    )
        return jsonify( { 'code':nation, 'ko':lang_ko, 'trans':transText } )

# 파파고 번역 연동( api 획득 )
Client_ID       = 'gHJNLgBDNvajDqTIaTPB'
Client_Secret   = '0PElXwLRwr'
'''
curl "https://openapi.naver.com/v1/language/translate" \ 
-H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
-H "X-Naver-Client-Id: gHJNLgBDNvajDqTIaTPB" \
-H "X-Naver-Client-Secret: 0PElXwLRwr" -v \
-d "source=ko&target=en&text=만나서 반갑습니다." -v
'''
def lang_transByPapago( text, na_code='en' ):
    # 사용자 인증키 설정
    client_id     = Client_ID
    client_secret = Client_Secret

    # 전송할 데이터(번역요청원문) URL 인코딩 처리( 목적: 한글깨짐 방지 )
    encText = urllib.parse.quote(text)

    # 통신 준비
    data     = "source={0}&target=ko&text={1}".format( na_code, encText) # {}: .format(0번인자, 1번인자) %: % format 
    url      = "https://openapi.naver.com/v1/papago/n2mt"

    # 요청객체 생성
    request = urllib.request.Request(url)

    # 해더 설정
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    # 통신
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        # 통신 성공 => 응답데이터를 json로드를 통해 파이썬의 객체로 리턴
        return json.load( response ) # papago 응답 예시는 json의 형태로 작성되어있음(딕셔너리 작성됨)
        #response_body = response.read()
        #print(response_body.decode('utf-8'))
    else:
        # 통신 실패
        return {}  # 번역결과 없음 -> 딕셔너리
        #print("Error Code:" + rescode)



# 4. 서버가동
if __name__=='__main__': # 조건문 이하 코드는 run.py가 직접 구동할때만 작동
    app.run(debug=True)

# html작성 시작-> service->public, templates 폴더 생성 -> template폴더 내 index.html생성 -> 14번줄 html 호출 코드 작성실시
# -> html에서 스크립트 함수 작성 
# service폴더 내에 ml폴더 생성 후 data: label.txt, 20190830.model 파일 붙여넣기



