def climb_stairs(n, memo=None):
    if memo is None:
        memo = {}

    # Базові випадки
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n in memo:
        return memo[n]

    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]


def check(n, expected):
    result = climb_stairs(n)
    print(f"Вхід: n = {n}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check(2, 2)
    check(3, 3)
    check(5, 8)
    check(45, 1836311903)
