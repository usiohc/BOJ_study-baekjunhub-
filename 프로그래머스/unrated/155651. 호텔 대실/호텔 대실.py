def solution(book_time):
    time = [0] * 1440
    times = []
    for bt in book_time:
        h, m = map(int, bt[0].split(':'))
        lh, lm = map(int, bt[1].split(':'))
        # times.append([h*60+m, lh*60+lm])
        for i in range(h*60+m-5, lh*60+lm+5):
            if 0<= i <1440:
                time[i] += 1

    print(time)
    
    return max(time)