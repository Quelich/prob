import math


def get_mean(array):
    if (array == None):
        return None
    sum = 0
    for i in array:
        sum = sum + i
    return sum / len(array)


def get_median(array):
    array.sort()
    n = len(array)
    if n % 2 != 0:  # odd
        return float(array[math.floor((n+1) / 2)])
    else:
        x1 = array[math.floor((n / 2)) - 1]
        x2 = array[math.floor((n/2 + 1)) - 1]
        return float((1/2) * (x1+x2))
    return null


def trim_array(array, percantage):
    if percantage > 100 or percantage < 0:
        return
    trimmed = []
    trim = math.ceil(len(array) * percantage / 100)
    i = 0
    while i < len(array):
        if i >= trim and i < len(array) - trim:
            trimmed.append(array[i])
        i = i + 1
    return trimmed


def get_variance():
    return 1


def get_standard_deviation():
    return 1


data_10 = [23, 60, 79, 32, 57, 74, 52, 70, 82, 36]

data_60 = [23, 60, 79, 32, 57, 74, 52, 70, 82,
           36, 80, 77, 81, 95, 41, 65, 92, 85,
           55, 76, 52, 10, 64, 75, 78, 25, 80,
           98, 81, 67, 41, 71, 83, 54, 64, 72,
           88, 62, 74, 43, 60, 78, 89, 76, 84,
           48, 84, 90, 15, 79, 34, 67, 17, 82,
           69, 74, 63, 80, 85, 61]

# mean = get_mean(data_60)
# median = get_median(data_60)
trimmed = trim_array(data_10, 40)
print(trimmed)
# print(f"length: {len(data_60)}\n")
# print(f"mean: {mean}\n", )
# print(f"median: {median}\n")
