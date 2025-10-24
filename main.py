def PrimeList(N):
    primes = []
    # 遍历2到N-1的所有数
    for num in range(2, N):
        is_prime = True
        # 判断是否为质数：检查2到sqrt(num)的数
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))  # 转为字符串，方便后续拼接
    # 用空格连接列表元素（末尾无空格）
    return ' '.join(primes)
