# 람다 방식

# 함수 정의 하기 귀찮은 개발자가 만든 방식
# "lambda 인자 : 리턴값" 이렇게 구성한다.
double = lambda x : x * 2
print(double(10))
print(double((1,2,4,5)))
print(double([1,2,3,4,5,7]))
# print(double({2,4,5,6,7})) # set, dict 안됨


# 람다 활용하기 : 리스트를 인자로 받는 경우.
nums = [1,2,3,4,5,6,7,8] # 이 경우, nums 인자를 위에다 미리 지정해 줘야 한다.
multiple_list = list(map(lambda x: x**2, nums))
print(multiple_list) # 위에 지정 됨 값의 데이터 형으로 리턴함

filtering = list(map(lambda x : x > 10, multiple_list))
print(filtering) # 부등호의 리턴은 boolean임

# 람다 활용하기 2 : 딕셔너리를 인자로 받는 경우
people = [
    {"name": "Hejin", "age": 28},
    {"name": "Mira", "age": 32},
    {"name": "Jinu", "age": 25},
    {"name": "Suyoung", "age": 30},
    {"name": "Taemin", "age": 27},
    {"name": "Yuna", "age": 24},
    {"name": "Minho", "age": 29},
    {"name": "Jisoo", "age": 26},
    {"name": "Hyun", "age": 31},
    {"name": "Sora", "age": 23}
]
# 정렬하기
sorted_age = sorted(people, key=lambda x : x["age"])
print(sorted_age)
# 역방향 정렬
reverse_sorted_age = sorted(people, key=lambda x : x["age"],reverse=True)
print(reverse_sorted_age)
"""
 파이썬이 인터프리트 언어라서 콘솔에 바로 함수를 정의하기 껄끄러운 경우 이런식으로 람다를 사용해서 실시간으로 상태를 확인 하는 모양
 코딩으로 문서를 남겨야 되는 경우 굳이 이따구 짓을 안하는게 좋지 않을 까.
 심플하게 기능을 구현할려면 이것도 좋은 것 같으데 익숙해 져야 좋은거지... 
"""

