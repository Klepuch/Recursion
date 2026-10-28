def my_pow(x, n):
    # Від'ємний степінь: x^(-n) = 1 / x^n
    if n < 0:
        return 1 / my_pow(x, -n)

    # Базовий випадок
    if n == 0:
        return 1.0

    # Рахуємо половину степеня лише один раз
    half = my_pow(x, n // 2)

    if n % 2 == 0:
        return half * half
    return half * half * x


def check(x, n, expected):
    result = f"{my_pow(x, n):.5f}"
    print(f"Вхід: x = {x:.5f}, n = {n}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check(2.0, 10, "1024.00000")
    check(2.1, 3, "9.26100")
    check(2.0, -2, "0.25000")
    check(1.0, 2147483647, "1.00000")
