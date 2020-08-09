"""
형변환
"""

# 암시적 형변환 (implicit casting)
num_int = 3
num_float = 3.14
num_new = num_int + num_float
print("type of `num_int` :", type(num_int))
print("type of `num_float` :", type(num_float))
print("type of `num_new` :", type(num_new))

# str -> int는 암시적으로 불가능.
num_int = 3
num_str = "6"
num_new = num_int + num_str
print("type of `num_int` :", type(num_int))
print("type of `num_str` :", type(num_str))
print("type of `num_new` :", type(num_new))

# 명시적 형변환 (explicit casting)
num_int = 3
num_str = "6"
num_str2 = int(num_str)
num_new = num_int + num_str2
print("type of `num_int` :", type(num_int))
print("type of `num_str` :", type(num_str))
print("type of `num_str2` :", type(num_str2))
print("type of `num_new` :", type(num_new))

"""
list, tuple, set, dict
"""

# list 자료형은 여러개의 데이터를 가지고 있는 배열 자료형입니다. 배열은 같은 타입만 가지고 있지 않아도 됩니다.
# 배열의 각 요소에는 인덱스(번호) 가 붙으며, 배열의 각 요소에 접근할 때는 인덱스를 사용해 접근합니다.
# 배열의 인덱스는 0부터 시작하며, (배열의 길이-1) 까지 존재합니다.
array = [0, 1, "2", True, "4", 5.0]
print(array)
print(type(array))
print(array[2], array[3])

# list 자료형은 선언 이후에도 내부 데이터를 변경할 수 있습니다.
array[2] = 4
print(array[2])

# list 객체는 insert 메소드를 통해 원하는 위치에 데이터을 추가할 수도 있습니다.
array.insert(1, "6")

# list 객체는 append 메소드를 통해 가장 마지막에 새 데이터를 추가할 수 있습니다.
array.append(7)

# dict 자료형은 키:값으로 데이터를 저장하는 딕셔너리 자료형입니다. 딕셔너리 자료형은 키와 값에 해당하는 데이터를 모두 저장하고, 값을 가져오기 위해서 키로 접근합니다.
dictionary = {}