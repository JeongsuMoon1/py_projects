1. 파이썬기반 데이터 과학
    -데이터 수집 
    -전처리 
    -적제 
    -분석 
    -시각화 
    -머신러닝
    -딥러닝(AI약한) 프로젝트 

2. github 를 이용한 공정관리
    - github.com 가입 및 로그인
    - git-scm.com 다운로드 및 설치 : 설치(선택박스 : 비쥬얼 스튜디오 깃 설정)
      설치시 editor를 vs code로 적용
    - github에 new -> repogitory 생성
      생성시 readme, .gitignore (python)으로 체크 및 생성
    - 로컬pc 프로젝트를 만들 위치에서
        public 이면
        -> 커맨드 실행 -> cd Desktop  
        -> $ git clone https://github.com/JeongsuMoon1/py_projects.git   (깃허브에서 관련프로젝트 클릭 후 초록색 버튼 clone을 클릭하고 폴더그림클릭하면 주소 복사됨)
* github private 학생: 보안설정할 수 있는 방법 찾아볼 것
    

- 최초 1회만
 만약, 프로젝트를 먼저 작업하다가, git를 사용한 경우
 1) git clone을 다른 위치에서 수행
 2) clone를 통해 만들어진 위치에 먼저 만들어진 프로젝트 내용을 이동
 3) vs code 에서 커밋(commin) and push 작업을 진행한다
 4) 단, 최초 수행시 git 오류가 나올 수 있고, 이 경우 터미널에서
 $git config --global user.email "appachi2@naver.com"
 $git config --global user.name "JeongsuMoon1" 
을 1회 수행해 주면(현재 프로젝트 위치에서) 처리된다.
 5) 앞으로는 clone 한 프로젝트 위치가 실제 작업할 곳이 된다
 집에서는 github clone을 받아주면 된다
 6) 

* source control -> 최초커밋(프로젝트 전체 구조 설정) 작성 -> commit 클릭 -> 에러 -> 
터미널에서 
git config --global user.email "appachi2@naver.com"
git config --global user.name "JeongsuMoon1"
을 작성 
-> 다시 커밋 시킴
-> 비쥬얼코드 윈도우 창에서 맨 밑에 파란줄에 있는 새로고침 버튼 클릭 -> github에 파일들이 들어와있는지 확인  
* 퇴근 시 저장 -> 소스컨트롤에서 다시 커밋시킨후 push 시킴 -> 깃허브에 파일 들어와있는지 확인
* 집에서 수정후 출근하여 다시 불러들일 경우 -> 소스컨트롤에서 ... 클릭 -> pull 클릭하면 vscode로 들어옴

