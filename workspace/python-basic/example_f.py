# 가위 바위 보 게임 버전 2

again = True
while again:
    selection = input("1.게임시작   2.종료 ( 작업을 선택하세요 ) : ")
    if selection == "1":
        # 1. 
        import random
        com_value = random.randint(1, 3)

        # 2. 
        user_value = input('1: 가위, 2: 바위, 3: 보를 선택하세요 (1 or 2 or 3 입력) : ')
        user_value = int(user_value)

        # 3.
        if (user_value == 1 and com_value == 3) or \
           (user_value == 2 and com_value == 1) or \
           (user_value == 3 and com_value == 2) :
            result = "WIN"
        elif user_value == com_value:
            result = "DRAW"
        else:
            result = "LOSE"

        print("YOU : {0}, COMPUTER : {1}, RESULT : {2}".format(user_value, com_value, result))
        pass
    elif selection == "2":
        print( "프로그램을 종료합니다." )
        again = False
    else:
        print( "지원하지 않는 명령입니다." )
    pass # 실행 내용은 없고 구문 구조를 갖추기 위해 사용하는 예약어

print( "End of Program" )