# Tuple, 자바 Record에 대응되는 자료 구조
# 값의 순서가 정해져 있고 각 인덱스 별 값의 변경이 불가능 하다

myTuple = (1,2,3)
yourTuple = (4,5,6)

plusTuple = myTuple+yourTuple
print(plusTuple)

complexTuple = myTuple * 3
print(complexTuple)

packingTuple = 2,'hi',"MyName", 2.9
print(packingTuple) # 이미 나열된 대상을 추가로 늘어 놓는 방식

complexTuple2 = packingTuple * 3
print(complexTuple2)

print(myTuple[0])

# myTuple[0] = 2 # 값을 못바꿈
print(myTuple)

# 튜플의 경우 아래와 같이 정의된 값의 갯수를 안다면 아래와 같이 나눠서 저장이 가능하다.
a,b,c = myTuple
print(a)
print(b)
print(c)

# 이 경우 값을 변경 가능, 튜플 상에서 각 인덱스 별로 값 수정이 되지 않음
a = 10
print(a)

# 많은 수의 숫자 튜플이 있음
alotTuple = (1,2,3,4,5,6,7,8,9)
# 이런 식의 변수 분할이 가능한데
first, *middle, last = alotTuple
print(first)
print(middle)
# 이 경우 중간에 모든 것을 감싸는 형식을 취한다.
print(last)


# 주 사용 용도는 함수의 리턴 값이 1개로 고정된 형태가 아닌 여러 개의 형태인 경우
# 자바에서는 map을 사용하여 명시적으로 처리 하나, 값의 순서를 굳이 아는 경우, 이런식으로 사용가능하다.
def main_max(numbers) :
    return min(numbers), max(numbers)

# 이렇게, 자바보다 편하다면 편하다
# 처리 속도도 빨르고, 데이터가 변하지 않아서 무결성 도움을 준다.
result = main_max(alotTuple)
print(result)

