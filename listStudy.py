# 리스트, 다 아는 그거다.
ordinaryList = ["apple","포도","banana","수박"]
print(ordinaryList)

# 파이썬에서 리스트 내장 함수 ㄱㄱ
# 추가하기
ordinaryList.append("peach")
print(ordinaryList)

# 특정위치에 값을 추가하기
ordinaryList.insert(3,"상추")
print(ordinaryList)

# 제거하기
ordinaryList.remove("banana")
print(ordinaryList)

# 값 변경하기
ordinaryList[0] = "appleCidar"
print(ordinaryList)

# 파이썬이 좋은건 리스트 끼리 합치기 곱하기 별개 다된다는 점
veges = ["파","양파","마늘","감자","tomato"]

# 리스트 합하기
begans = veges + ordinaryList
print(begans)

# 리스트 반복하기
repeat_veges = veges * 4
print(repeat_veges)

# 슬라이싱1 : from ~ to (start : end)
sub_begans = begans[1:7]
print(sub_begans)

# 슬라이싱2 : form ~ to , 3칸씩 띄어서 (start : end : step)
sub_repeat_veges = repeat_veges[0:10:3]
print(sub_repeat_veges)