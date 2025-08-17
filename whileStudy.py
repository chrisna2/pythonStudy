# while 문
cnt = 0
while cnt < 5:
    print("현재 카운드 : ",  cnt)
    cnt+=1

cnt2 = 0
while True: # 무한 루프 가겠다.
    if cnt2 == 10 :
        break # 끊는 기준임 ㅇㅇ
    # Tab 바꿈 위치 중요 이래서
    print(cnt2)
    cnt2 += 1 # ++ 같은 고급언어는 안됨다.

cnt3 = 0
while cnt3 < 5 :
    cnt3 += 1
    if cnt3 == 3 :
        continue # 3은 프린트 안함 ㅇㅇ
    print(cnt3)
    
# while에도 else가 붙는다. 
cnt4 = 0 
while cnt4 < 3 : # 조건이 false 가 되면 else로 빠짐.
    print("루프 내부에는 : ", cnt4)
    cnt4 += 1
else : 
    print("루프 정상 종료 ㅇㅇ")

# 무한 루프 : 입력을 받아야 끝남 -> input & response 형태의 구조 활용
while True:
    response = input("exit 할겨? : ")
    if response == "exit":
        break
    print("명령 수행 : ", response)
