# 엔트리 포인트 -> (중요한 이유) 여기서부터 경로를 따진다.
# 1. 모듈 가져오기
from  flask import Flask, render_template, request, jsonify, redirect # 클래스가 나온다(대문자로)
from ml import detect_lang # __init__를 끌고온다, ml(패키지)를 들고온다
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

        return jsonify( { 'code':nation, 'ko':lang_ko } )


# 4. 서버가동
if __name__=='__main__': # 조건문 이하 코드는 run.py가 직접 구동할때만 작동
    app.run(debug=True)

# html작성 시작-> service->public, templates 폴더 생성 -> template폴더 내 index.html생성 -> 14번줄 html 호출 코드 작성실시
# -> html에서 스크립트 함수 작성 
# service폴더 내에 ml폴더 생성 후 data: label.txt, 20190830.model 파일 붙여넣기



