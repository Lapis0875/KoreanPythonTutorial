for i in range(1, 60):
    answer = str(i)
    if '3' in answer or '6' in answer or '9' in answer:
        number_counts = [answer.count('3'), answer.count('6'), answer.count('9')]
        clap_count = 0
        for count in number_counts:
            if count >= 1:
                clap_count = clap_count + count
        print("짝"*clap_count)
    else:
        print(answer)