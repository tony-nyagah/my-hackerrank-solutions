"""A hashset/dictionary is pretty useful here."""


def sock_merchant(n: int, ar: list[int]) -> int:
    count = {}
    pair_list = []

    for num in ar:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for x in count.values():
        pair_list.append(x // 2)

    return sum(pair_list)


print(sock_merchant(7, [1, 2, 1, 2, 1, 3, 2]))
print(sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
