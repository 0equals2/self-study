student1={"학번":1000,"이름":"홍길동","학과":"열공학과"}
student2={"학번":1001,"이름":"강감찬","학과":"체육학과"}
student3={"학번":1002,"이름":"이순신","학과":"물리학과"}
student4={"학번":1003,"이름":"신사임당","학과":"열공학과"}

student_list=[]
student_list.append(student1)
student_list.append(student2)
student_list.append(student3)
student_list.append(student4)
while True:
    print("┌--------------------------------------------┐")
    print("│학생관리 프로그램 V1.0 created by 유영은    │")
    print("├--------------------------------------------┤")
    print("│1.전체출력 2.검색 3.신규 학생추가     0.종료│")
    print("└--------------------------------------------┘")
    number = int(input("명령을 입력해주세요 : "))
    while number!=1 and number!=2 and number!=3 and number!=0:
        num=int(input("잘못된 명령입니다. 다시 입력하세요.:"))

    if number==1:
        print("┌--------------------------------------------┐")
        print("│전체 학생 목록                              │")
        print("└--------------------------------------------┘")
        for i in student_list:
            print("학번:%s, 이름:%s, 학과:%s"%(i["학번"],i["이름"],i["학과"]))
        print("==출력종료==")
        continue
    elif number==2:
        print("┌--------------------------------------------┐")
        print("│검색 메뉴를 선택하세요.                     │")
        print("├--------------------------------------------┤")
        print("│1.이름검색 2.학과검색                       │")
        print("└--------------------------------------------┘")
        num=int(input("검색메뉴를 선택하세요:"))
        while num!=1 and num!=2:
            num=int(input("잘못된 명령입니다. 다시 입력하세요.:"))
        if num==1:
            name=input("검색할 이름을 입력하세요:")
            for i in student_list:
                if (i["이름"] == name) :
                    print("학번:%s, 이름:%s, 학과:%s"%(i["학번"],i["이름"],i["학과"]))
                    break
            print("==출력종료==")
            continue
        
        else:
            depart=input("검색할 학과를 입력하세요:")
            for i in student_list:
                if (i["학과"] == depart) :
                    print("학번:%s, 이름:%s, 학과:%s"%(i["학번"],i["이름"],i["학과"]))
            print("==출력종료==")
            continue
        
    elif number==3:
        num_s=input("학번을 입력하세요:")
        name=input("이름을 입력하세요:")
        depart=input("학과를 입력하세요:")
        student_list.append({"학번":num_s,"이름":name,"학과":depart})
        print("신규학생이 추가되었습니다. 전체 목록을 출력합니다.")
        print("┌--------------------------------------------┐")
        print("│전체 학생 목록                              │")
        print("└--------------------------------------------┘")
        for i in student_list:
            print("학번:%s, 이름:%s, 학과:%s"%(i["학번"],i["이름"],i["학과"]))
        print("==출력종료==")
        continue
    
    else:
        print("┌--------------------------------------------┐")
        print("│프로그램을 종료합니다.                      │")
        print("└--------------------------------------------┘")
        break
    
        
