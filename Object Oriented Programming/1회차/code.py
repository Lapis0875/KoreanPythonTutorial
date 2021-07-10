# 클래스 선언하기
class MyClass:
    def method(self):
        print('안녕 클래스!')

    def sum(self, a, b):
        self.number = a + b

    def print_number(self):
        print(self.number)


# 객체 생성하기
instance = MyClass()
instance.method()
instance.sum(1, 2)          # 이 줄을 주석처리해보세요!
instance.print_number()     # 주석처리하면 이 줄에서 오류가 발생합니다. 클래스의 속성은 생성자 __init__ 에서 정의해주는게 좋아요!


# 클래스 생성자
class Person:
    def __init__(self, name, age):  # 여기서 정의한 파라미터들은 객체 생성시 전달해야 합니다.
        """
        클래스의 생성자입니다.
        """
        self.name = name  # 클래스의 속성(attribute) 를 정의할 때, self.(속성 이름) = (값) 처럼 사용합니다.
        self.age = age

    def greeting(self):
        print('안녕하세요,', self.name)  # 앞서 정의한 속성값을 사용할 때, self.(속성 이름) 으로 사용합니다.

    def grow(self):
        self.age += 1  # 클래스의 속성값은 다시 할당할 수 있습니다.


person = Person('홍길동', 22)  # __init__ 에서 정의한 파라미터들을 전달합니다.
person.greeting()


# 클래스 상속하기
class Animal:
    def __init__(self, specie, age):
        self.specie = specie
        self.age = age

    def info(self):
        print('종 :', self.specie, ', 나이 :', self.age)

    def sound(self):
        print('정해지지 않은 동물의 울음소리입니다')


class Dog(Animal):          # Animal 클래스를 상속하는 Dog 클래스를 만듭니다.
    def __init__(self, age):
        # 부모 클래스를 호출할 때, super()을 사용합니다.
        super().__init__('dog', age)

    def sound(self):
        print('멍멍!')


class Cat(Animal):
    def __init__(self, age):
        super().__init__('cat', age)

    def sound(self):
        print('냐옹 냐옹!')


dog = Dog(5)
dog.info()
dog.sound()

cat = Cat(3)
cat.info()
cat.sound()
