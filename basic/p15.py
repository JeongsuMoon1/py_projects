# 예외처리
#   > 풀코드 형태 확인 
# 밑에 소스코드는 풀코드 형태임 try 자동완성에서 제일 긴것
try:
    print(1)
    # print(1/0) # 여기서 에러 발생 -> 3번 부터 실행 -> 그다음 주석처리함: 결과는 1,2,4,5
    print(2)
except Exception as e: # 예외가 발생하면 진입 # 자바에서는 exception e 
    print(3, e)
else:       #예외가 없으면 진입, else는 필수적인것이 아니다
    print(4)
finally:    # 무조건 마지막으로 진입
    print(5)








