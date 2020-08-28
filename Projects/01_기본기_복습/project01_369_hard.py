def player_turn(prev):
    player = input("당신의 차례입니다 : ")
    answer = str(prev + 1)
    # 3, 6, 9가 포함되는 차례인지 확인
    if '3' in answer or '6' in answer or '9' in answer:
        # 포함될 경우 숫자 대신 박수를 침
        if player != "짝":
            print("박수를 쳐야 하는 차례입니다! 당신이 졌습니다.")
            return -1
    else:
        # 앞서 출력된 숫자의 다음 숫자가 아닌지 확인
        if player != answer:
            print("잘못된 숫자입니다! 당신이 졌습니다")
            return -1

    # 현재 라운드의 숫자를 반환함
    return int(answer)


def computer_turn(prev):
    answer = str(prev + 1)

    # 3, 6, 9가 포함되는지 확인
    if '3' in answer or '6' in answer or '9' in answer:
        # 포함될 경우 숫자 대신 박수를 침
        print("👏")
    else:
        # 포함되지 않을 경우 숫자를 출력함
        print(answer)

    # 입력값을 반환함
    return int(answer)


def game():
    prev = 0
    rounds = 0
    while True:
        # 새로운 라운드
        rounds = rounds + 1
        if rounds % 2 == 1:
            # 플레이어의 차례
            prev = player_turn(prev)
            if prev == -1:
                # 플레이어가 졌을 경우
                break
        else:
            # 컴퓨터의 차례
            prev = computer_turn(prev)


game()
