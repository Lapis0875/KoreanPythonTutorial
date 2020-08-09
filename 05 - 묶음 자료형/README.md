# 5강 자료형 2편
이번 강의에서는 파이썬의 형변환(Casting)과 묶음 자료형(타입) list, dict, tuple, set 에 대해 알아봅니다.

## 형변환
형변환은 한 데이터를 기존의 자료형과 다른 자료형으로 변환하는 방법입니다.

파이썬에서는, 굳이 명시하지 않아도 알아서 형변환이 진행되는 경우와 명시적으로 변환해줘야만 하는 경우가 있습니다.

### 암시적 변환
```python
num_int = 3
num_float = 3.14
num_new = num_int + num_float
print("type of `num_int` :", type(num_int))
print("type of `num_float` :", type(num_float))
print("type of `num_new` :", type(num_new))
```
위 코드의 출력 결과는 아래와 같습니다 :
```css
type of `num_int` : <class 'int'>
type of `num_float` : <class 'float'>
type of `num_new` : <class 'float'>
```
int와 float 모두 숫자 자료형이기 때문에 사칙연산이 정의되어 있습니다. 그러나, int형과 float형이 표현 가능한 범위는 다릅니다. float 타입이 int 타입보다 표현 가능한 범위가 더 크기 때문에, int 타입과 float 타입의 연산 결과는 float 타입이 됩니다.

그러나, 이런 경우는 암시적인 변환을 진행할 수 없습니다.
```python
num_int = 3
num_str = "6"
num_new = num_int + num_str
print("type of `num_int` :", type(num_int))
print("type of `num_str` :", type(num_str))
print("type of `num_new` :", type(num_new))
```

위 코드의 출력 결과는 아래와 같습니다 : 
```css
Traceback (most recent call last):
  File "D:/Study/Python/YH/05 - 묶음 자료형/types02.py", line 16, in <module>
    num_new = num_int + num_str
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
str 타입과 int 타입은 암시적으로 변환할 수 없습니다. str 타입과 int 타입의 합이 정의되지 않았기 때문이죠.

### 명시적 변환
그렇다면, str 타입을 **명시적**으로 int형으로 바꿔주면 됩니다.
파이썬에서 명시적으로 타입 변환을 진행할 때에는, int(), float()와 같이 사용합니다.
```python
num_int = 3
num_str = "6"
num_str2 = int(num_str)
num_new = num_int + num_str2
print("type of `num_int` :", type(num_int))
print("type of `num_str` :", type(num_str))
print("type of `num_str2` :", type(num_str2))
print("type of `num_new` :", type(num_new))
```

위 코드의 출력 결과는 아래와 같습니다 :
```css
type of `num_int` : <class 'int'>
type of `num_str` : <class 'str'>
type of `num_str2` : <class 'int'>
type of `num_new` : <class 'int'>
```
str 타입인 `num_str`을 명시적으로 int 타입으로 변환해 `num_str2`에 저장했습니다. 그 결과, `num_str`의 타입은 str로 확인되지만 `num_str2`의 타입은 int로 확인됩니다.
