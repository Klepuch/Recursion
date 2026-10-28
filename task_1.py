def print_reverse(s, index=0):
    # Базовий випадок: дійшли до кінця рядка - нічого не друкуємо
    if index == len(s):
        return
    # Спочатку друкуємо решту рядка (вона опиниться попереду)
    print_reverse(s, index + 1)
    # Потім поточний символ
    print(s[index], end="")


def demo(s, expected):
    print(f'Вхід: "{s}"')
    print("Вихід:     ", end="")
    print_reverse(s)
    print()
    print(f"Очікувано: {expected}")
    print()


if __name__ == "__main__":
    demo("tiger", "regit")
    demo("hello", "olleh")
    demo("a", "a")
