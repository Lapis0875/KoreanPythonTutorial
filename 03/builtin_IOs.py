# 기본 출력함수 print입니다. print의 파라미터로 전달된 데이터를 콘솔에 출력해요.
print("Hello World!")
print(100)
print(True)
print(3.14)

# print 함수에 여러개의 데이터를 쉼표(,) 로 구분해 전달해주면, 전달받은 데이터들을 순서대로, 공백 한 칸(띄어쓰기 생각하시면 되요!)으로 구분해서 출력해줘요.
print(100, True, "Hello!", 3.14)

# type 함수를 사용해, 변수가 담고 있는 데이터 혹은 직접 입력한 데이터의 자료형을 알 수 있어요.
print(type(100))
print(type(True))
print(type("Hello World!"))
print(type(3.14))

# 기본 입력함수 input입니다. input의 파라미터로는 콘솔에 출력할 문자열을 전달하며, input 함수는 콘솔을 통해 입력받은 데이터를 반환합니다.
answer = input("정답을 입력해주세요! : ")
print("입력하신 정답은", answer, "입니다.")