# type 함수를 사용해, 변수가 담고 있는 데이터 혹은 직접 입력한 데이터의 자료형을 알 수 있어요.
print(type(100))
print(type(True))
print(type("Hello World!"))
print(type(3.14))

# 기본 입력함수 input입니다. input의 파라미터로는 콘솔에 출력할 문자열을 전달하며, input 함수는 콘솔을 통해 입력받은 데이터를 반환합니다.
answer = input("정답을 입력해주세요! : ")
print("입력하신 정답은", answer, "입니다.")