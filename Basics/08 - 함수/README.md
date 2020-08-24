# 8강 함수
![function image](./Function_machine2.svg)

수학에서의 함수는 위 사진처럼 입력값에 어떠한 작업을 통해 출력값을 만들어냅니다.
프로그래밍에서의 함수도 수학에서의 함수와 유사한 개념입니다.

## 파이썬에서 함수 선언하고 사용해보기
```python
# 파이썬에서 함수 선언하기
# arg : 함수에 전달하는 파라미터(인자)
# return : 함수가 반환하는 결과값
def my_function(arg):
    return "Hello " + arg + "!"

result = my_function("World")
print(result)
```
파이썬에서 함수는 def 키워드를 사용해 선언합니다.
() 괄호 안에는 함수가 전달받아야 하는 파라미터를,
return 키워드로는 함수가 반환하는 값을 정의합니다.
위 코드를 실행하게 되면, 다음과 같은 결과를 얻을 수 있습니다.
```css
Hello World!
```
arg 에 해당하는 부분이 my_function에 전달한 파라미터 값인 `"World"` 로 바뀌었고, `my_function("World")` 의 결과는 result에 반환되었습니다.

함수는 원하는대로, 필요에 따라 다양하게 선언할 수 있습니다.
파라미터와 반환값을 모두 가지는 함수나,
```py
def add(num1, num2):
    return num1 + num2


print(add(1, 2))
```
파라미터는 가지지만 값을 반환하지 않는 함수,
```py
def print_message(msg):
    print(msg)


print_message("Python 강좌")
```
파라미터는 가지지 않지만 값을 반환하는 함수,
```py
def return_something():
    return 5


print(return_something())
```
파라미터도 없고 값도 반환하지 않는 함수도 있습니다.
```py
def task():
    print("파라미터도 없고 값도 반환하지 않습니다!")


task()
```

***

[예제 코드](/Basics/08%20-%20함수/function.py)</br>
[이전 강좌](/Basics/07%20-%20반복문/README.md)</br>
[다음 강좌](/Projects/01_기본기_복습/README.md)
