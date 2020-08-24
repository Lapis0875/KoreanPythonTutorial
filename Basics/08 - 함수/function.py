# 파이썬에서 함수 선언하기
# arg : 함수에 전달하는 파라미터(인자)
# return : 함수가 반환하는 결과값
def my_function(arg):
    return "Hello " + arg + "!"


result = my_function("World")
print(result)


# 1. 파라미터와 반환값이 모두 존재하는 함수
def add(num1, num2):
    return num1 + num2


print(add(1, 2))


# 2. 파라미터는 존재하지만 값을 반환하지 않는 함수
def print_message(msg):
    print(msg)


print_message("Python 강좌")


# 3. 파라미터가 존재하지 않지만 값을 반환하는 함수
def return_something():
    return 5


print(return_something())


# 4. 파라미터도 존재하지 않고 값도 반환하지 않는 함수
def task():
    print("파라미터도 없고 값도 반환하지 않습니다!")


task()

