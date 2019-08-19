2019년 8월 19일 오후 2시부터 진행 수업
[[ 자연어 처리 ]]
1. 개요
 - 한글 자연어 처리를 파이썬으로 수행하는 과정
 - 모듈명 : 코엘앤파이
 - KoNLPy
  1) https://konlpy-ko.readthedocs.io/ko/v0.4.3/
  2) 파이썬의 간결하고, 우아하고 강력한 스트링 연산 기능을 최대한 살렸다
  3) 여러 형태소 분석기들이 포함 : 꼬꼬마, 한나눔, MeCab-Ko 등등..(품질재단 공유 엑셀에서 내용 확인 참조)
  4) 자연어 처리에 필요한 각종 사전, 말뭉치, 도구, 튜토리얼 제공
  5) 쉽다

2. 설치과정( 아나콘다 base 작업환경에서 설치하겠다)
 - 반드시 순서대로 할것
 - 코엘앤파이 설치
     $ pip install konlpy : 아나콘다 작업환경 base에서 설치를 진행한다(프롬프트 실행)
 - jdk 설치
     $java -version : 자바 1.8 버전 설치되어있는지 확인
     $환경변수 추가
     > 윈도우 : JAVA_HOME=jdk경로설정
       ->내피씨->우클릭->속성->고급 시스템설정->환경변수
       ->USER에 대한 사용자변수 새로만들기-> 변수이름 : JAVA_HOME                        -> 확인
                                             변수값   : C:\Program Files\Java\jre1.8.0_211
       
       
     > 맥: export JAVA_HOME=$(/user/libexec/java_home)
 - python 으로 자바 라이브러리를 사용하는 모듈 설치
     > 자신이 Java라고 생각하고 Java 라이브러리를 사용할 수 있는 모듈
     > $conda install -c conda-forge jpype1
     > $conda install jpype1
       -> 주의사항(실패사유) : 운영체계의버전, JDK버전, 주피터경로상에 한글이 있거나, PC이름이 한글이거나 하면 간혹 안될수 있다.
       
 - python용 라이브러리 nltk 설치
    $ base 가상환경은 nltk가 설치되어 있다
    $ python (위의 install이 끝나면 프롬프트에서 작성시작하면 된다)
    > import nltk
    > nltk.download() : 1시간 정도 소요될 수 있다
    > NLTK Downloader에서 -> all -> 다운로드
    > 설치중 연결이 끊기면 다시 시도, 프로레스가 잡고 있어서 안된다면 콘솔까지 닫고 다시시도
      완료후 
    > ctrl + z
 
 - Raw text용 워드크라우드, 젠심
    $ pip install wordcloud gensim

3. 코엘엔파이 형태소 분석기

 - Hannanum
   > 1999년부터 KAIST 시맨틱웹 연구 센터(SWRC)에서 개발(자바)
 - Kkma
   > SNU의 지능형 데이터 시스템(IDS)연구소에서 개발 -> 자바로개발, 형태소 분석, 자연언어 처리시스템
 - Mecab
   > 일본의 형태소 분석기와 교토대학 정보학과 연구에서 개발한 POS tagger을 Mecab-ko로 변경하여 한국어에 적용한 것
 - Okt (이전 이름은 트위터twiter)
   > Will Hohyon Ryu, 개발한 scala로 연구개발, 한국어 토크나이저
 - Komoran
   > 2013년도, Shinware에서 개발, 자바로 작성된 새로운 오픈소스 한국어 형태학 분석기
 
4. 형태소 분석기별 함수들의 의미

5. pos함수에 대한 형태소별 의미















































































































