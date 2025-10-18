def PrimeList(N):
    primes = []
    # 遍历 2 到 N - 1 的每个数，判断是否为质数
    for num in range(2, N):
        is_prime = True
        # 试除判断，只需检查到 num 的平方根（优化计算量）
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 用空格连接质数，末尾无空格
    return " ".join(primes)
