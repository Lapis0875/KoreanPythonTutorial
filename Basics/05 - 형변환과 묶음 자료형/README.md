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
  File "파이썬 강좌/Basics/05 - 묶음 자료형/casting_and_containers.py", line 16, in <module>
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
list 자료형은 선언 이후에도 내부 데이터를 변경할 수 있습니다.
또, 다양한 메소드를 지원해 내부의 데이터를 자유롭게 조작할 수 있습니다.
```python
# list 자료형은 선언 이후에도 내부 데이터를 변경할 수 있습니다.
array = [0, 1, "2", True, "4", 5.0]
print("2번 인덱스 :", array[2])
array[2] = 4
print("2번 인덱스 :", array[2])

# list 객체는 insert 메소드를 통해 임의의 위치에 데이터을 추가할 수도 있습니다.
array.insert(1, "6")
print('1번 인덱스에 "6" 추가', array)
# list 객체는 append 메소드를 통해 리스트의 가장 끝부분에 새 데이터를 추가할 수 있습니다.
array.append(7)
print("끝에 7 추가", array)
# list 객체는 remove 메소드를 통해 원하는 데이터를 한 개 씩 지울 수 있습니다.
# 이 때, 지우려는 데이터가 2개 이상 존재할 경우, 가장 왼쪽에 있는 데이터를 삭제합니다.
array.remove("4")
print('"4" 삭제', array)
# list 객체는 extend 메소드를 통해 다른 list, tuple 등의 객체에 저장된 데이터를 가져올 수 있습니다.
array.extend([6, 7, 8, 9])
print("[6, 7, 8, 9] 확장", array)
# extend 메소드에 문자열을 전달할 경우, 문자열의 각 글자가 list 내부에 따로따로 저장됩니다.
array.extend("안녕하세요")
print('"안녕하세요" 확장', array)
```
위 코드의 실행 결과는 다음과 같습니다 :
```css
2번 인덱스 : 2
2번 인덱스 : 4
1번 인덱스에 "6" 추가 [0, '6', 1, 4, True, '4', 5.0]
끝에 7 추가 [0, '6', 1, 4, True, '4', 5.0, 7]
"4" 삭제 [0, '6', 1, 4, True, 5.0, 7]
[6, 7, 8, 9] 확장 [0, '6', 1, 4, True, 5.0, 7, 6, 7, 8, 9]
"안녕하세요" 확장 [0, '6', 1, 4, True, 5.0, 7, 6, 7, 8, 9, '안', '녕', '하', '세', '요']
```

### tuple
tuple 자료형은 list와 마찬가지로, 여러개의 데이터를 타입과 무관하게 저장할 수 있습니다. 
그러나, list 자료형은 생성 이후에도 내부에 저장된 데이터들을 변경할 수 있지만, tuple은 선언할 때 저장한 데이터들을 이후에 변경할 수 없습니다.
프로그래밍 용어로는, list는 mutable(변경 가능) 하고 tuple은 immutable(변경 불가능) 하다고 말합니다.
```python
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[2])
my_tuple[2] = 7
```
위 코드의 출력 결과는 다음과 같습니다 : 
```css
(0, 1, 2, 3, 4, 5)
2
Traceback (most recent call last):
  File "파이썬 강좌/Basics/05 - 묶음 자료형/casting_and_containers.py", line 59, in <module>
    my_tuple[2] = 7
TypeError: 'tuple' object does not support item assignment
```
### set
set 자료형은 수학에서 배우는 집합과 같은 개념의 자료형입니다.
set 자료형은 list나 tuple과는 달리, 데이터의 중복이 허용되지 않습니다.
또, list나 tuple과는 달리, 내부의 데이터들이 순서를 가지지 않아 인덱싱을 사용할 수 없습니다.
따라서, `A[0]` 처럼 사용하게되면 오류가 발생합니다.
```python
# set 자료형은 수학에서 배우는 `집합` 과 같은 자료형입니다.
A = {1, 2, 3, 4, 5}
# set 자료형은 데이터의 중복이 허용되지 않습니다.
B = set([3, 4, 5, 6, 6, 7, 7, 7, 8])
print(A, B)
print(type(A), type(B))
# set 자료형은 앞서 배웠던 list, tuple과는 다르게 내부의 데이터들이 순서를 가지지 않아 인덱싱을 사용할 수 없습니다.
print(A[0])
```
위 코드의 실행 결과는 다음과 같습니다 :
```css
{1, 2, 3, 4, 5} {3, 4, 5, 6, 7, 8}
<class 'set'> <class 'set'>
Traceback (most recent call last):
  File "파이썬 강좌/Basics/05 - 묶음 자료형/casting_and_containers.py", line 68, in <module>
    print(A[0])
TypeError: 'set' object is not subscriptable
```
set 자료형은 합집합, 교집합 등 집합의 연산들을 지원합니다.
```python
# set 자료형은 집합의 연산들을 사용할 수 있습니다.
A = {1, 2, 3, 4, 5}
B = set([3, 4, 5, 6, 6, 7, 7, 7, 8])
# & 기호 혹은 intersection() 메소드를 사용해 두 집합의 교집합을 구할 수 있습니다.
intersection = A & B
print("A와 B의 교집합", intersection)
print(type(intersection))
print(A.intersection(B), B.intersection(A))
# | 기호 혹은 union() 메소드를 사용해 두 집합의 합집합을 계산할 수 있습니다.
union = A | B
print("A와 B의 합집합", union)
print(type(union))
print(A.union(B), B.union(A))
# - 기호 혹은 difference() 메소드를 사용해 두 집합의 차집합을 계산할 수 있습니다.
A_diff_B = A - B
B_diff_A = B.difference(A)
print("A와 B의 차집합 (A-B)", A_diff_B, type(A_diff_B))
print("B와 A의 차집합 (B-A)", B_diff_A, type(B_diff_A))
```
위 코드의 실행 결과는 다음과 같습니다 :
```css
A와 B의 교집합 {3, 4, 5}
<class 'set'>
{3, 4, 5} {3, 4, 5}
A와 B의 합집합 {1, 2, 3, 4, 5, 6, 7, 8}
<class 'set'>
{1, 2, 3, 4, 5, 6, 7, 8} {1, 2, 3, 4, 5, 6, 7, 8}
A와 B의 차집합 (A-B) {1, 2} <class 'set'>
B와 A의 차집합 (B-A) {8, 6, 7} <class 'set'>
```
set 자료형은 데이터의 추가/삭제를 지원합니다.
```python
A = {1, 2, 3, 4, 5}
# set 자료형에 새 데이터를 추가하려면, add() 메소드를 사용할 수 있습니다.
A.add(6)
print(A)
# set 자료형의 여러개의 새 데이터를 추가하려면, update() 메소드를 사용할 수 있습니다.
A.update([7, 8, 9, 10])
print(A)
# set 자료형에서 특정 값을 지우고 싶다면, remove() 메소드를 사용할 수 있습니다.
A.remove(7)
print(A)
```
위 코드의 실행 결과는 다음과 같습니다 :
```css
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
{1, 2, 3, 4, 5, 6, 8, 9, 10}
```


### dict
dict 자료형은 **딕셔너리** 라고 부르는 자료형으로, 
앞서 list와 tuple에서는 인덱스를 사용해 내부 데이터에 접근했다면 딕셔너리는 **키** 를 사용해 내부 데이터에 접근합니다.
딕셔너리는 **`키 : 값`** 의 형태로 정의합니다.
```python
# dict 자료형은 키:값으로 데이터를 저장하는 딕셔너리 자료형입니다. 
# 딕셔너리 자료형은 키와 값에 해당하는 데이터를 모두 저장하고, 값을 가져오기 위해서 키로 접근합니다.
dictionary = {"key": "value", "name": "홍길동", "age": 36}
print(dictionary, type(dictionary))
print(dictionary["name"])
```
위 코드의 실행 결과는 다음과 같습니다 :
```css
{'key': 'value', 'name': '홍길동', 'age': 18} <class 'dict'>
홍길동
```
딕셔너리에 데이터를 추가하거나 삭제할 때는 아래와 같이 추가할 수 있습니다.
```python
# dict 자료형에 새 데이터를 추가할 때는 아래와 같이 추가할 수 있습니다.
dictionary = {"key": "value", "name": "홍길동", "age": 36}
# 단일 데이터 추가 :
dictionary["school"] = "영훈고등학교"
print(dictionary)
# 여러개의 데이터 추가 :
dictionary.update({"grade": 2, "class": 5})
print(dictionary)
# dict 자료형에서 데이터를 제거할 때는 pop() 메소드를 사용합니다. pop() 메소드는 제거한 값을 반환합니다.
age = dictionary.pop("age")
print(age)
print(dictionary)
```
위 코드의 실행 결과는 다음과 같습니다 :
```css
{'key': 'value', 'name': '홍길동', 'age': 18, 'school': '영훈고등학교'}
{'key': 'value', 'name': '홍길동', 'age': 18, 'school': '영훈고등학교', 'grade': 2, 'class': 5}
17
{'key': 'value', 'name': '홍길동', 'school': '영훈고등학교', 'grade': 2, 'class': 5}
```
***

[예제 코드 보기](/Basics/05%20-%20형변환과%20묶음%20자료형/casting_and_containers.py)

[<- 이전 강좌](/Basics/04%20-%20연산자/README.md) /
[다음 강좌 ->](/Basics/06%20-%20조건문/README.md)