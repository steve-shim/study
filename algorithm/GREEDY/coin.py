def change_money(N, wallet):
    total = 0
    for coin in wallet:
        count = N // coin
        N = N - (coin*count)
        total += count
        
    print("거스름돈으로 받을 총 동전 갯수는? : %d 개" %total)

N = 1260
wallet = [500, 100, 50, 10]

#결과 출력
change_money(N, wallet)