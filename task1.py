def left_diff(a: list, b: list) -> list:
    return list(set(a) - set(b))


if __name__ == '__main__':
    # input data
    list1 = [i for i in range(100)]
    list2 = [i for i in range(-50, 50)]

    # logic
    print(left_diff(list1, list2))
