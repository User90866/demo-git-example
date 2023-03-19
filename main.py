def demo_zip():
    values1 = list(range(2,10))
    values2 = list(range(10, 29, 3))
    print(values1)
    print(values2)
    print("zip(values1, values2) = ", list(zip(values1, values2)))
    for v1, v2 in zip(values1, values2):
        print("v1 =", v1, ";  v2 =", v2, ";  sum =", v1+v2)

    print("=" * 30)
    values3 = list(range(20, -7, -5))
    print(list(values3))
    print(list(zip(values1, values2, values3)))

    for v1, v2, v3 in zip(values1, values2, values3):
        print("v1 =", v1, ";  v2 =", v2, ";  v3 =", v3, ";  sum =", v1 + v2 + v3)
def demo_map():
    list1 = [1, 2, 3, 5]
    list2 = [5, 3, 2, 0]

    list_of_powers = list(
        map(pow, list1, list2)
    )
    print(list_of_powers)

def main():
    # print("Hello main")
    demo_map()
    # demo_zip()


if __name__ == "__main__":
    main()