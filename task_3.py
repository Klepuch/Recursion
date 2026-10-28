def fib(n, memo=None):
    if memo is None:
        memo = {}

    # Базові випадки
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Якщо вже рахували - повертаємо збережене значення
    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def check(n, expected):
    result = fib(n)
    print(f"Вхід: n = {n}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check(2, 1)
    check(3, 2)
    check(4, 3)
    check(10, 55)
    check(30, 832040)
