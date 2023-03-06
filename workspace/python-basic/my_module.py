# 변수 만들기
module_name = "my module"

# 함수 만들기
def f():
    print("function in module")

# 클래스 만들기
class Cls:
    def f(self):
        print("function in module.class")

# 테스트 코드
# c = Cls() # import 할 때에도 실행
# c.f()     # import 할 때에도 실행

if __name__ == "__main__": # python my_moudle.py 방식으로 실행하면 True (import 할 때에는 False)
    # 테스트 코드
    c = Cls() # import 할 때에는 실행 X
    c.f()     # import 할 때에는 실행 X