# for 문
fruits = ['바나나',"사과","포도","복숭아","딸기"]
for f in fruits :
    print(f)

# for 문을 받을 수 있는건 정해져 있는게 읎다.
# 문자열
for char in "hello world people":
    print(char)

# 튜플
for tup in (1,2,3,4,5,6):
    print(tup)

# 딕셔너리 : 인자는 키의 나열임
person = {"name":  "Jinu", "age": 25}
for key in person :
    print(key, person[key])


# break ,continue
for number in range(100):
    if number == 5 :
        break
    print(number)
# java랑 똑같이 0부터 시작임 ㅇㅇ
for number in range(100):
    if number % 17 == 0 :
        print(number)
    else :
        continue

# for - else : 이건 그냥 보통 for문이 종료 되면 마지막에 끝이라고 표시 하려고 만든 방법임 
for number in range(10) :
    print(number)
else :
    print("숫자 세기 종료함 ㅇㅇ")
    

# Range 활용 
# for i in range(stop) : 여기서 멈추 겠다고
for number in range(10) :
    print(number)

# for i in range(start, stop) : 범위 지정 가능
for i in range(10, 15):
    print(i)

# for i in range(start, stop, step) : 범위의 값을 몇 스텝 기준으로
for i in range(10, 15, 2):
    print(i)

# Range 응용
# list
veges = ["상추","토마토","양파","고구마","감자"]
for i in range(len(veges)):
    print(veges[i])
# 역순
for i in range(len(veges)-1, 0, -1):
    print(veges[i])


# 리스트 컴프리핸션 : 리스트 자동으로 만들기
# 리스트
squares = [x**2 for x in range(12)]
print(squares)
# 튜플 -> 안됨?
squares_tup = (x*2 for x in range(3))
print(squares_tup)
# 세트 -> 됨 ㅇㅇ
squares_set = {x*2 for x in range(3)}
print(squares_set)