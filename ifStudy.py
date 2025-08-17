# if 문 : 파이썬의 if 문은 텝의 기능이 꽤나 중요. 자바랑 달리 명시적이지 않아서 기능 구분하려면 정신 차리고 코드를 깔끔하게 작성해야 된다.

age = 11
if age >= 18 and age < 60 :
    if age < 45 :
        print(f"이제 {age}면 이제 애 아님. ㅇㅇ")
    elif age >= 45 and age < 50 :
        print(f"이제 {age}면 이제 겁에 질릴 나이지. ㅇㅇ")
    else :
        print(f"이제 {age}인데 아직도 일한다. 님 좀 짱인듯. ㅇㅇ")
# 얘네들은 이것 마져도 줄여 쓴다. elif
elif age >= 60 :
    print(f"이제 {age}면 이제 은퇴 ㄱㄱ. ㅇㅇ")
else :
    print(f"이제 {age}면 아직 애 임. ㅇㅇ")

# 명시적인거 보다 편한게 좋다는게 파이선개발자
status = f"이제 {age}면 이제 애 아님. ㅇㅇ" if age >= 18 else f"이제 {age}면 아직 애 임. ㅇㅇ"
print(status)
# 가독성이 좋은지는 미지수임
