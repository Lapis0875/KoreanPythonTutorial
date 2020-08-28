# # 항등 연산자
# print(5 == 5, 5 == 1, "5" == 5)
# print(5 != 3, 3 != 3, "5" != 5)
#
# # 대소비교 연산자
# print(5 > 3, 3 >= 3)
# print(5 < 3, 3 <= 3)
#
# # in 연산자
# if 'a' in "abc":
#     print("a는 abc 안에 있습니다!")
#
# # not 연산자
# if not True:
#     print("if문의 조건이 True입니다!")
#
# # 조건문
# answer = input("원하는 조건문을 입력하세요 : ")
#
# if answer == "if":
#     # if문 등 : 로 끝나는 구문 내부에서 실행될 코드는, 들여써야 합니다.
#     print("if문을 실행합니다.")
# elif answer == "elif1":
#     # elif문은 앞선 if문이 거짓일 때 이어서 진행되는 if문으로,
#     print("첫 번째 elif문을 실행합니다.")
# elif answer == "elif2":
#     # elif문은 여러개 사용할 수 있습니다.
#     print("두 번째 elif문을 실행합니다.")
# else:
#     # else문은 앞선 if, elif문이 모두 거짓일 때 실행되는 마지막 조건문입니다.
#     print("else문을 실행합니다.")
    
# 두개의 조건이 모두 True일 때 True가 되는 and 연산자
answer = input("영단어를 입력하세요 > ")
if 'a' in answer and 'e' in answer:
    print("입력받은 영단어에는 a와 e가 모두 포함됩니다!")
else:
    print("입력받은 영단어에는 a와 e가 모두 포함되는것은 아닙니다...")

# 두개의 조건중 하나라도 True이면 True가 되는 or 연산자
answer = input("영단어를 입력하세요 > ")
if 'a' in answer or 'e' in answer:
    print("입력받은 영단어에는 a 또는 e가 포함됩니다!")
else:
    print("입력받은 영단어에는 a와 e가 모두 포함되지 않습니다...")
