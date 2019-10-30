def closest_power(base, num):
    result = 0
    if base > num:
        result = 0
    elif base == num:
        result = 1
    else:
        for i in range(1, int(num)):
            if abs(base**i - num) <= abs(base**(i + 1) - num):
                result = i
                break
    return result
