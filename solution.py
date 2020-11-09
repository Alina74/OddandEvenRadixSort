input_arr = [3, 4, 1, 2, 16, 27, 13]


def sort_by_radix(source, expression):
    length = len(source)

    res = [0] * length
    numbers = [0] * 10

    for i in range(0, length):
        index = (source[i] / expression)
        numbers[int(index % 10)] += 1

    for i in range(1, 10):
        numbers[i] += numbers[i - 1]

    i = length - 1
    while i >= 0:
        index = (source[i] / expression)
        res[numbers[int(index % 10)] - 1] = source[i]
        numbers[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(source)):
        source[i] = res[i]


def radix_sort(source):
    maximum = max(source)
    radix = 1
    while maximum / radix > 0:
        sort_by_radix(source, radix)
        radix *= 10


def solve(source):
    odd_arr = [x for x in source if x % 2 == 1]
    even_arr = [x for x in source if x % 2 == 0]
    print(even_arr)

    radix_sort(odd_arr)
    radix_sort(even_arr)

    odd_arr.reverse()

    res = even_arr + odd_arr

    return res


result = solve(input_arr)
print(result)
