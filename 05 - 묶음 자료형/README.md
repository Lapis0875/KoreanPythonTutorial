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

## 파이썬의 묶음 자료형
이전 시간에 배웠던 int, float, str, bool 등의 타입 이외에도, 파이썬에는 다양한 타입이 존재합니다.
오늘은 그중 여러개의 데이터를 저장할 수 있는 list, tuple, set, dict에 대해 알아보려 합니다.

### list
list 자료형은 여러개의 데이터를 가지고 있는 배열 자료형입니다. 배열은 같은 타입만 가지고 있지 않아도 됩니다.
배열의 각 요소에는 인덱스(번호) 가 붙으며, 배열의 각 요소에 접근할 때는 인덱스를 사용해 접근합니다.
배열의 인덱스는 0부터 시작하며, (배열의 길이-1) 까지 존재합니다.
```python
array = [0, 1, "2", True, "4", 5.0]
print(array)
print(type(array))
print(array[2], array[3])
```
위 코드의 출력 결과입니다 :
```css
[0, 1, '2', True, '4', 5.0]
<class 'list'>
2 True
```

### tuple
tuple 자료형은 list와 마찬가지로, 여러개의 데이터를 타입과 무관하게 저장할 수 있습니다. 그러나, list 자료형은 생성 이후에도 내부에 저장된 데이터들을 변경할 수 있다면 tuple은 선언할 때 저장한 데이터들을 이후에 변경할 수 없습니다.
프로그래밍 용어로는, list는 mutable(변경 가능) 하고 tuple은 immutable(변경 불가능) 하다고 합니다.

### set
set 자료형은 수학에서 배우는 집합과 같은 개념의 자료형입니다. 같은 데이터가 중복되어 저장될 수 없으며, 합집합, 차집합 등의 집합 연산들이 가능합니다.

### dict
dict 자료형은 **딕셔너리** 라고 부르는 자료형으로, 앞서 list와 tuple에서는 인덱스를 사용해 내부 데이터에 접근했다면 딕셔너리는 **키** 를 사용해 내부 데이터에 접근합니다.
딕셔너리는 **`키 : 값`** 의 형태로 정의합니다.