# 딕셔너리 (Dictionary) , 자바의 map , js의 JSON 익히 알고 있는 그 구조
# 지겨운 구조 이지만 몇가지 유용한 기능에 대하여 정리 추가

# 구조는 JSON가 동일 함
person = {
    "name" : "hyunkke",
    "locale" : "SEOUL",
    "sex" : "male",
    "age" : 34   
}
# 딕셔너리 메서드 : java의 map이랑 같이 내부에 지원되는 함수가 있다.

# keys : map의 keys와 동일 List(key)
keys = person.keys()
print(keys)

# valuse : map의 Values 와 동일, List(value)
values = person.values()
print(values)

# items : 모든 쌍을 가져옴, List(Tuple) 형태
items = person.items();
print(items)

# 딕셔너리 컴프레션 : 간단함 문법으로 딕셔너리를 생성하는 방법 -> 목업 데이터 생성에 도움?
squares = {x: x*x for x in range(6)} # 0 ~ 6번의 반복이 이루어지고 x는 키 x*x는 밸류
print(squares)
# 별개 다 된다.
multiName = {x : "hunkee"*x for x in range(6)}
print(multiName)