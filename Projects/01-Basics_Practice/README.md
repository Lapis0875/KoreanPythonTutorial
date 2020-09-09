# 프로젝트 1 
앞서 공부한 Basics 의 1강~8강의 내용을 복습하고자, 369게임을 제작해보고자 합니다.
369 게임의 규칙은 아래와 같습니다 :
> 사용자는 숫자를 말합니다.
> 만약 숫에 3, 6, 9가 포함된다면, 숫자 대신에 박수를 칩니다.

파이썬으로 구현하게 된다면 어떻게 구현하면 될까요?
간단한 힌트를 드릴테니 직접 만들어보며 복습하는 시간을 가져봅시다 :D
1. input() 함수로 사용자의 입력 받기 - 3강
2. 입력받은 값에 3, 6, 9가 들어있는지 확인하기 : if문, in 연산자 - 6강
3. print() 함수로 값 출력하기 - 3강
4. 반복문 사용하기 - 7강

예시 코드는 아래 두가지가 있습니다.

쉬운 버전 : 반복문을 돌며 369게임의 규칙에 맞게 숫자를 출력합니다.
[코드 보기](./project01_369_easy.py)

어려운 버전 : 컴퓨터와 플레이어가 번갈아가면서 게임을 진행하며, 플레이어가 오답을 입력하면 게임을 종료합니다.
[코드 보기](./project01_369_hard.py)