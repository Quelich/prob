import math


def get_mean(A):
    if (A == None):
        return None
    sum = 0
    for i in A:
        sum = sum + i
    return sum / len(A)


def get_median(A):
    A.sort()
    n = len(A)
    if n % 2 != 0:  # odd
        return float(A[math.floor((n+1) / 2)])
    else:
        x1 = A[math.floor((n / 2)) - 1]
        x2 = A[math.floor((n/2 + 1)) - 1]
        return float((1/2) * (x1+x2))
    return null


def trim_array(A, percantage):
    if percantage > 100 or percantage < 0:
        return
    trimmed = []
    trim = math.ceil(len(A) * percantage / 100)
    i = 0
    while i < len(A):
        if i >= trim and i < len(A) - trim:
            trimmed.append(A[i])
        i = i + 1
    return trimmed


def get_variance(A, mean):
    n = len(A)
    sum = 0
    for i in A:
        sum = sum + math.pow((i - mean), 2)
    return sum / (n - 1)


def get_standard_deviation(variance):
    if variance < 0:
        raise ValueError("The variance must be greater than zero!")
    return math.sqrt(variance)


# data_10 = [23, 60, 79, 32, 57, 74, 52, 70, 82, 36]
data_10 = [7.07, 7.00, 7.10, 6.97, 7.00, 7.03, 7.01, 7.01, 6.98, 7.08]
mean = get_mean(data_10)
variance = get_variance(data_10, mean)
std_devi = get_standard_deviation(variance)
print("mean: ", mean)
print(f"variance: {variance}")
print(f"standard deviation: {std_devi}")


data_60 = [23, 60, 79, 32, 57, 74, 52, 70, 82,
           36, 80, 77, 81, 95, 41, 65, 92, 85,
           55, 76, 52, 10, 64, 75, 78, 25, 80,
           98, 81, 67, 41, 71, 83, 54, 64, 72,
           88, 62, 74, 43, 60, 78, 89, 76, 84,
           48, 84, 90, 15, 79, 34, 67, 17, 82,
           69, 74, 63, 80, 85, 61]


# mean = get_mean(data_60)
# median = get_median(data_60)
# trimmed = trim_array(data_10, 40)
# print(trimmed)
# print(f"length: {len(data_60)}\n")
# print(f"mean: {mean}\n", )
# print(f"median: {median}\n")
