n = input('몇번째 까지 반복할까요? > ')
for i in range(1, int(n) + 1):
    answer = str(i)
    clap_count = answer.count('3') + answer.count('6') + answer.count('9')
    print(f'debug > clap_count = {clap_count}')
    if clap_count >= 1:
        print("짝" * clap_count)
    else:
        print(answer)
