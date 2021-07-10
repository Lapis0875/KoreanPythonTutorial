# 7강 반복문
프로그래밍 언어들은 다양하지만, 지원하는 반복문의 종류는 대체로 비슷합니다.

### range()
range는 원하는 범위의 정수 데이터를 보관하는 객체입니다.
range(시작, 끝+1, 숫자 사이의 간격) 으로 사용합니다.
```python
# range
nums = range(0, 10)     # 0 ~ (10-1) 의 숫자가 담긴 리스트 비슷한 객체
print(nums, type(nums))
print(list(nums))       # list 객체로 형변환

nums_even = range(0, 10, 2)
print(nums_even, list(nums_even))
```
위 코드의 실행 결과는 다음과 같습니다 :
```css
range(0, 10) <class 'range'>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(0, 10, 2) [0, 2, 4, 6, 8]
```

### for
for문은  Iterable 한 (추후 강의에서 설명할게요. 일단은 여러개의 데이터를 가지고 있어 각각의 데이터를 순회할 수 있다는 걸로 이해하시면 될 것 같아요.)
객체에 저장된 데이터를 하나씩 가져와 순회하는 반복문입니다. for ~ each 스타일의 반복문입니다.
for 문은 고유한 코드블럭을 가지므로, for 문 내부의 코드는 한 칸 들여써야 합니다.
```python
for i in range(0, 5):
    print(i)
```
위 코드의 실행 결과입니다 :
```css
0
1
2
3
4
```

이전 강의에서 설명한 list, tuple, dict 자료형 또한 Iterable 합니다.
```python
my_list = ["안녕하세요", 0, 1, 2, True, 4.0]
for i in my_list:
    print(i)
```
```css
안녕하세요
0
1
2
True
4.0
```

```python
my_tuple = (0, 1, 2, False, "이것은 튜플입니다.")
for i in my_tuple:
    print(i)
```
```css
0
1
2
False
이것은 튜플입니다.
```
```python
my_dict = {
    "name": "홍길동",
    "age": 17,
    "school": "영훈고등학교",
    "grade": 1,
    "class": 1
}

# 딕셔너리의 키로 순회하기
print("딕셔너리의 키로 순회하기 : ")
for key in my_dict.keys():
    print(key)

# 딕셔너리의 값으로 순회하기
print("딕셔너리의 값으로 순회하기 : ")
for value in my_dict.values():
    print(value)

# 딕셔너리의 (키, 값) 으로 구성된 튜플로 순회하기
print("딕셔너리의 (키, 값)으로 순회하기 : ")
for kv in my_dict.items():
    print(kv)
```
```css
딕셔너리의 키로 순회하기 : 
name
age
school
grade
class
딕셔너리의 값으로 순회하기 : 
홍길동
17
영훈고등학교
1
1
딕셔너리의 (키, 값)으로 순회하기 : 
('name', '홍길동')
('age', 17)
('school', '영훈고등학교')
('grade', 1)
('class', 1)
```

### while
while 문은 주어진 조건이 참일 때 반복하는 구문입니다. while 문 또한 고유한 코드블럭을 가지므로, while 문 내부의 코드는 한 칸 들여써야 합니다.
```python
i = 0
while i < 5:
    print(i)
    i = i + 1
```
```css
0
1
2
3
4
```

### break
break 키워드를 사용해 현재 진행중인 반복문을 나갈 수 있습니다.
```python
i = 5
while i > 0:
    i = i - 1
    print(i)
    if i == 3:
        break
```
```css
4
3
```

### continue
continue 키워드를 사용해 코드 실행을 건너뛸수 있습니다.
```python
for i in range(100):   
    if i % 2 == 0:
        continue
    print(i)
```

```css
1
3
5
...
95
97
99
```

### 무한루프
반복문이 영원히 끝나지 않고 무한정 진행되는 것을 **`무한루프`** 라고 말합니다.

while 문은 조건이 True일때 반복하므로, `while True:` 처럼 작성해 무한 루프를 만들 수 있습니다.
```python
n = 0
while True:
    n = n + 1
    print("무한루프입니다 :", n, "회 반복중입니다.")
```
***

[예제 코드 보기](./loop.py)

[<- 이전 강좌](../06-조건문/README.md) /
[다음 강좌 ->](../08-함수/README.md)
