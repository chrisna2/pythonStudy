# 함수 , 메서드

# 함수 정의
def greet(name):
    return f"hello, {name}"

# 함수 정의 : 아쉽게도 오버로딩은 지원 안됨 자연스럽게
def greet2(name1, name2):
    return f"hello, {name1}, {name2}"

# print(greet()) # 파라미터가 없음 에러남
print(greet("hyunkee"))
print(greet2("minji","sooyoung"))
# 순서 따위 무시 하고 싶으면 무지성으로 정의된 파라미터 명을 쓰면됨 
print(greet2(name2="jenifer", name1="tablo"))

# 파이썬은 함수의 값을 지정 할때 기본값을 셋팅 가능 하다.
# 그리고 파이썬은 인터프리트 언어라서 같은 이름으로 메서드를 정의 하면 덮어 씌어진다. 고래서 오버로딩이 안됨 ㅇㅇ
def greet(name="수지"):
    return f"hello, {name}"

print(greet())

# 오버로딩이 안되서 짜증이 나면 파라미터를 가변 인자로 설정해서 사용 하면 됨
# * 한개는 인자의 값이 튜플의 형태로 들어온다는 뜻임
def greet(*names):
    print("hello ")
    for name in names:
        print(f", {name}") # 반복문에 변수 또는 정의된 인자를 프린트 하려면 f 써주자

print(greet("hejin","mira","jinu","suyoung"))


# ** 두개는 인자의 값이 딕셔너리 형태로 온다는 뜻임
def greet2(**names):
    print("hello thoses are your job")
    for key in names:
        print(f", {key} = {names[key]}")

## 이 경우 함수를 호출 하는 방법좀?
greet2(hejin="developer", mira="designer", jinu="manager", suyoung="intern")




