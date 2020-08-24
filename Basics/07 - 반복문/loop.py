# # range
# nums = range(0, 10)     # 0 ~ (10-1) 의 숫자가 담긴 리스트 비슷한 객체 (추후 고급강의에서 설명)
# print(nums, type(nums))
# print(list(nums))       # list 객체로 형변환
#
# nums_even = range(0, 10, 2)
# print(nums_even, list(nums_even))
#
# for i in range(0, 5):
#     print(i)
#
# my_list = ["안녕하세요", 0, 1, 2, True, 4.0]
# for i in my_list:
#     print(i)
#
# my_tuple = (0, 1, 2, False, "이것은 튜플입니다.")
# for i in my_tuple:
#     print(i)
#
# my_dict = {
#     "name": "홍길동",
#     "age": 17,
#     "school": "영훈고등학교",
#     "grade": 1,
#     "class": 1
# }
#
# # 딕셔너리의 키로 순회하기
# print("딕셔너리의 키로 순회하기 : ")
# for key in my_dict.keys():
#     print(key)
#
# # 딕셔너리의 값으로 순회하기
# print("딕셔너리의 값으로 순회하기 : ")
# for value in my_dict.values():
#     print(value)
#
# # 딕셔너리의 (키, 값) 으로 구성된 튜플로 순회하기
# print("딕셔너리의 (키, 값)으로 순회하기 : ")
# for kv in my_dict.items():
#     print(kv)
#
# print("while 문 확인")
# i = 0
# while i < 5:
#     print(i)
#     i = i + 1
#
# print("while 문 + break")
# i = 5
# while i > 0:
#     i = i - 1
#     print(i)
#     if i == 3:
#         break

print("무한루프")
n = 0
while True:
    n = n + 1
    print("무한루프입니다 :", n, "회 반복중입니다.")