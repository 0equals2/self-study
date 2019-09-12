while True:
    s=input("문자열을 입력하세요:")
    r=[] #비어있는 list 생성
    #for문을 이용한 중복 검사(index 이용)
    for i in range(len(s)):
        if i==0: #첫번째 문자 list에 넣기
            r.append(s[i])
        elif s[i]!=s[i-1]:#연속된 중복이 없는 문자 list에 넣기
            r.append(s[i])
    #결과출력
    print("입력값:%s"%s)
    print("결과값:",end="")
    for i in r:
        print(i,end="")
    print("\n")
