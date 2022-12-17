import math


def get_mean(array):
    sum = 0
    for i in array:
        sum = sum + i
    return sum / len(array)


def get_median(array):
    array.sort()
    print(array)
    n = len(array)
    if n % 2 != 0:  # odd
        return float(array[math.floor((n+1) / 2)])
    else:
        return float((1/2) * (array[math.floor((n / 2)) - 1] + array[math.floor((n/2 + 1)) - 1]))
    return null


def trim_array(array, percantage):
    trimmed = []
    trim = len(array) * percantage / 100

    return 1


def get_variance():
    return 1


def get_standard_deviation():
    return 1


data = [23, 60, 79, 32, 57, 74, 52, 70, 82,
        36, 80, 77, 81, 95, 41, 65, 92, 85,
        55, 76, 52, 10, 64, 75, 78, 25, 80,
        98, 81, 67, 41, 71, 83, 54, 64, 72,
        88, 62, 74, 43, 60, 78, 89, 76, 84,
        48, 84, 90, 15, 79, 34, 67, 17, 82,
        69, 74, 63, 80, 85, 61]

mean = get_mean(data)
median = get_median(data)
trimmed = trim_array(array, 10)
print(f"length: {len(data)}\n")
print(f"mean: {mean}\n", )
print(f"median: {median}\n")
