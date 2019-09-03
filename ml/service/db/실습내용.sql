# sys_config 의 데이터는 오직 1개로 만들어서 관리
select model_ver from sys_config;

# 함수명 selectModelInfo 를 db/__init__.py에 구현
# ml/__init__.py에서 댕겨서 경로를 설정해준다
select dir, label from predict_model_mgr
where ver=(select model_ver from sys_config);