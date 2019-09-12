
import random #난수 사용을 위한 random 모듈 불러오기
while True:
    user=int(input("가위바위보를 선택하세요 (1.주먹, 2.가위, 3.보자기):"))
    com=random.randint(1,3) #1에서 3사이의 임의의 수를 반환
    print("============================================")
    if user==1:
        user="주먹"
    elif user==2:
        user="가위"
    else:
        user="보자기"
    print("당신의 선택은 (%s)입니다." % (user))#사용자 선택값 출력
    #숫자가 아닌 문자로 출력하기 위해 if문을 활용하여 출력
    if com==1:
        com="주먹"
    elif com==2:
        com="가위"
    else:
        com="보자기"
    print("컴퓨터의 선택은 (%s)입니다." % (com))#컴퓨터 선택값 출력
#숫자가 아닌 문자로 출력하기 위해 if문을 활용하여 출력

#승자계산 및 결과 출력
    if user==com:
        print("비겼습니다!")#선택이 같을 경우 무조건 비겼습니다 출력
    elif user=="주먹" and com=="가위":
       print("당신의 승리!")#user가 주먹일 때 승리 출력
    elif user=="주먹" and com=="보자기":
        print("컴퓨터 승리!")#user가 주먹일 때 패배 출력
    elif user=="가위" and com=="주먹":
        print("컴퓨터 승리!")#user가 가위일 때 패배 출력
    elif user=="가위" and com=="보자기":
        print("당신의 승리!")#user가 가위일 때 승리 출력
    elif user=="보자기" and com=="주먹":
        print("당신의 승리!")#user가 보자기일 때 승리 출력
    else:
        print("컴퓨터 승리!")#user가 보자기일 때 패배 출력
    #가능한 경우의 수를 앞에서 다 입력했으므로 elif가 아닌 else 사용
