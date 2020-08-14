# 항등 연산자
print(5 == 5, 5 == 1, "5" == 5)
print(5 != 3, 3 != 3, "5" != 5)
print(5 > 3, 3 >= 3)
print(5 < 3, 3 <= 3)

# 조건문
answer = input("원하는 조건문을 입력하세요 : ")

if answer == "if":
    # if문 등 : 로 끝나는 구문 내부에서 실행될 코드는, 들여써야 합니다.
    print("if문을 실행합니다.")
elif answer == "elif1":
    # elif문은 앞선 if문이 거짓일 때 이어서 진행되는 if문으로,
    print("첫 번째 elif문을 실행합니다.")
elif answer == "elif2":
    # elif문은 여러개 사용할 수 있습니다.
    print("두 번째 elif문을 실행합니다.")
else:
    # else문은 앞선 if, elif문이 모두 거짓일 때 실행되는 마지막 조건문입니다.
    print("else문을 실행합니다.")
