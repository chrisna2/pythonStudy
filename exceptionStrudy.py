# 예외 처리
try: 
    number = int(input("정수 입력해 주세용 : "))
    devison = 10/number
except ValueError:
    print("숫자를 입력하라고 멍청아")
except ZeroDivisionError:
    print("0으로는 못나눠 수학 모르니?")
else:
    print("결과는 ", devison)
finally:
    print("프로그램 종료 ㅇㅇ")


# 예외 처리 2
try:
    number = int(input("정수 입력해 주세용 : "))
    devison = 10/number
except (ValueError,ZeroDivisionError):
    print("숫자를 입력하라고 멍청아")
    print("0으로는 못나눠 수학 모르니?")
else:
    print("결과는 ", devison)
finally:
    print("프로그램 종료 ㅇㅇ")

# 예외 처리 3
try:
    number = int(input("정수 입력해 주세용 : "))
    devison = 10/number
except Exception as e :
    print("이런 에러 발생함 : ", e)
else:
    print("결과는 ", devison)
finally:
    print("프로그램 종료 ㅇㅇ")