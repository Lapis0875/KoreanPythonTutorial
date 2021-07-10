# Python Tutorial
이 저장소는 파이썬 강좌 자료들을 보관하는 깃허브 저장소입니다.
영훈고등학교 프로그래밍 스터디 소동아리에서 사용하기 위한 목적으로 제작되었으나, 공익읗 위해 오픈소스로 공개합니다.
강좌는 아래의 목차로 이루어져 있습니다.
</br></br>

## [기초 강좌 : Basics](Basics/README.md)
프로그래밍 언어의 가장 기본적인 부분들인 설치부터 함수까지 배워보고자 합니다.
1. [파이썬 설치](Basics/01-파이썬 설치하기/README.md)
2. [변수와 기본 자료형](Basics/02-변수와 타입/README.md)
3. [기본 입출력 함수](Basics/03-기본 콘솔 입출력/README.md)
4. [사칙 연산자](Basics/04-operators/README.md)
5. [형변환 (Casting) 과 묶음 자료형](Basics/05-casting_and_collections/README.md)
6. [흐름 제어문 1 : if ~ elif ~ else 와 조건문](Basics/06-conditions/README.md)
7. [흐름 제어문 2 : for, while 반복문](Basics/07-loops/README.md)
8. [함수](Basics/08-function/README.md)
</br></br>

## [프로젝트 01 : 기본기 강좌 복습](Projects/01_기본기_복습/README.md)
기본 강좌에서 배운 내용을 복습하며, 간단한 프로그램을 만들어봅시다.
1. [369 게임 만들기](Projects/01-Basics_Practice/README.md)
</br></br>

## [Tips : 프로그래밍을 하면서 알아두면 도움되는 팁 - 1부](Tips/README.md)
1. [특강 1) 구글링을 습관화하자](Tips/01-Google_It/README.md)
2. [특강 2) Stack Overflow](Tips/02-StackOverflow/README.md)
3. [특강 3) 정규표현식](Tips/03-RegEx/README.md)
</br></br>

## [파이썬의 문법들 - 1부](Python_Grammers/README.md)
1. [파일 입출력](Python_Grammers/01-FileIO/README.md)
2. [문자열(str) 을 다룰 때 유용한 메소드들]()
3. in 키워드
4. 타입이란 무엇인가? & 타입 힌트
</br></br>

## [객체지향 패러다임 : Object Oriented Programming](Object Oriented Programming/README.md)
1. 객체지향 프로그래밍은 어떤 패러다임인가? & 지금까지 써오던 방식과 비교해보기
2. 클래스와 객체
3. 클래스가 가지는 특성 (캡슐화, 상속, ...)
4. 클래스 상속
5. 클래스 상속 과정에서 일어날 수 있는 문제점 (다중상속, 다이아몬드 상속, ...)
6. 파이썬의 클래스와 매직 메소드
</br></br>

## [프로젝트 02 : 고민중](Projects/02_고민중/README.md)
객체지향 패러다임에 대해 공부한 내용들을 복습하고자 진행하는 프로젝트입니다.
1. 간단한 텍스트 RPG 만들기
</br></br>

## [파이썬의 문법들 - 2부](Python_Grammers/README.md)
1. del 키워드
2. with 키워드
3. iterator와 generator
4. list , dict, set, generator comprehension


## [라이브러리 활용해보기]()
1. 파이썬 내장 라이브러리 1 - random, time, datetime
2. 파이썬 내장 라이브러리 2 - logging
3. HTTP 요청 라이브러리 1 - urllib, requests
4. HTML 파싱 라이브러리 - BeautifulSoup4
5. XML 파싱 라이브러리 - xml
6. 백엔드 서버 라이브러리 - flask, django
</br></br>

## [프로젝트 04 : 공개된 API 활용해보기]()
고급 3강에서 배웠던 라이브러리들을 활용한 프로젝트를 진행합니다.
네이버, 구글, 카카오 등 공개되어있는 api 자신이 선택해서 해당 api를 활용해보는 프로젝트
</br></br>

## [Tips : 프로그래밍을 하면서 알아두면 도움되는 팁 - 2부](Tips/README.md)
1. [특강 3) 정규표현식 regex](Tips/03-RegEx)
</br></br>

## [함수형 패러다임 : Functional Programming]()
1. 함수형 패러다임은 무엇인가?
2. 1급 객체로써의 함수, 그리고 고계함수
3. 클로져(Closure) 와 데코레이터(Decorator)
</br></br>

## [프로젝트 05]()
( 고민중 )
</br></br>

## [파이썬으로 다뤄보는 동시성(Concurrent)와 병렬성(Parallelism)]()
1. 동시성과 병렬성, 그리고 이를 위한 모듈 threading, multiprocessing, asyncio
2. Threading - 스레드(Thread)의 개념과 스레드의 특징, 그리고 그로 인해 나타나는 문제들과 해결법
3. Multiprocessing - 프로세스(Process)의 개념 과 특징, 스레드와의 비교
4. Asynchronous  - 비동기 프로그래밍의 개념과 특징
5. Futures - 고수준 병렬처리 API concurrent.futures
</br></br>

## [프로젝트 06]()
고급 5강에서 공부한 동시성과 병렬성을 활용해, 오래걸리는 작업의 소요시간을 단축해보자.
( 고민중 )
</br></br>

## [파이썬은 어떻게 구현되었는가]()
1. 파이썬 인터프리터, CPython
2. 파이썬의 고질적인 문제들 - GIL
3. 파이썬의 다른 구현체들 : Jython, Cython, IronPython, PyPy
4. C언어로 구현된 CPython : ctypes 모듈
</br></br>

## [메타클래스 type]()
1. type의 정체, 메타클래스
2. 모든 클래스의 최상위 클래스는 무엇일까?
3. type을 활용해 동적으로 클래스 정의하기
4. type을 상속하는 새 메타클래스 만들기
</br></br>

## [프로젝트 07]()
( 고민중 )
</br></br>

#### [파이썬 강좌를 마무리하며...]()
