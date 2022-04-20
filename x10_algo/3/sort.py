arr = [9, 5, 1, 4, 0, 7]


def quick_sort_v1(arr, l, r):
    if l >= r:
        return
    x = l
    y = r
    base = arr[l]
    while x <= y:
        while x <= y and arr[y] > base:
            y = y - 1
        while x <= y and arr[y] < base:
            x = x + 1
        if x <= y:
            arr[y], arr[x] = arr[x], arr[y]
            x = x + 1
            y = y + 1

    quick_sort_v1(arr, l, y)
    quick_sort_v1(arr, x, r)


quick_sort_v1(arr, 0, 5)
