# 머신러닝 모델을 기반으로 예측 함수를 구성하겠다
# 1. 모델부터 로드(올린다)만든다 ( 작동환경은 => 콘다에서 베이스(root)에서 작업한다)
from sklearn.externals import joblib
import os
import re
import json


# 서버가 재가동될 때 => 예측모델을 로드하므로 => 이 위치를 최신으로 갱신해준다
# 예측모델

#  학습데이터 로드 ( 머신러닝한 데이터를 끌고온다 )
# 모든 경로는 entry 포인트를 기준으로 따진다( run.py 기준의 관점에서는 ml->clf_lang으로 흘러간다)
# 툴에서는 작업 환경이 py_projects/ml/service에서 작업하엿다
ml_model_file = './ml/clf_lang_20190830.model'
clf = joblib.load( ml_model_file )

# 정답 로드
ml_label_file = './ml/clf_lang_labels.label'
with open(ml_label_file, 'r') as f:
    clf_label = json.load(f)    

# 판정 함수
def detect_lang( text ):  # 여기서-> 최종부분 -> run.py에서 29번줄로 넘긴다
    # 데이터 백터화
    text = text.lower()                # 소문자로 
    p1 = re.compile( '[^a-zA-Z ]*' )   # 영어를 제외한 불필요한 단어 제거용 정규식 (한글의 비중이 영어보다 높을 경우 한글로 처리한다, 또는, 한글만 두고 날린다.)
    text = p1.sub('', text)            # 정제작업
    if not text.strip():               # .strip: 공백날리기(부수적인 기능) 
        return None, None
    cnts = [ 0 for n in range(26) ]     # 백터화된 데이터를 담을 그릇
    asc_a, asc_z, asc_ws = ord('a'), ord('z'), ord(' ')  # 판단의 기준값 획득
    for ch in text:                     # 모든 글자 반복
        n = ord(ch)                     # 아스키화
        if asc_a <= n <= asc_z:         # 알파벳이 맞으면
            cnts[ n - asc_a ] += 1      # 빈도증가
    total_cnt = sum(cnts)               # 전체빈도계산
    if not total_cnt: # total_cnt == 0: # 빈도가 없다 -> 알파벳아님 -> 판독불가
        return None, None
    freq = list(map( lambda x: x/total_cnt, cnts )) # 정규화
    

    # 예측판정
    res = clf.predict( [freq] )
    if res:     
        return res[0], clf_label[ res[0] ] # 이건 그냥 문자열 나열한 것

    # 아래처럼 출력
    else:
        return None, None










