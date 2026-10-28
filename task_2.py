class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    # Базовий випадок: порожній список або один вузол - міняти нічого
    if head is None or head.next is None:
        return head

    first = head
    second = head.next

    # Рекурсивно обробляємо решту списку після пари
    first.next = swap_pairs(second.next)
    # Другий вузол стає першим
    second.next = first

    return second


# ---------- Допоміжні функції (теж без циклів) ----------

def build_list(values, index=0):
    """Створює зв'язаний список з Python-списку."""
    if index == len(values):
        return None
    return ListNode(values[index], build_list(values, index + 1))


def to_list(node):
    """Перетворює зв'язаний список у звичайний Python-список."""
    if node is None:
        return []
    return [node.val] + to_list(node.next)


def check(values, expected):
    result = to_list(swap_pairs(build_list(values)))
    print(f"Вхід: head = {values}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 2, 3, 4], [2, 1, 4, 3])
    check([], [])
    check([1], [1])
    check([1, 2, 3], [2, 1, 3])
