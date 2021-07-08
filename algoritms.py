import random
import math


def distribution_by_days(quantity, days):
    if days == 0:
        return [quantity]
    else:
        today = random.randint(math.ceil(3 * quantity / 16), math.ceil(5 * quantity / 16))
        return [today] + distribution_by_days(quantity - today, days - 1)


def regenerate_distribution(left_quantity, left_days, distribution):
    distribution = eval(distribution)
    b = distribution[-left_days:]
    now = sum(b)
    if left_quantity > now:
        for i in range(len(b)):
            b[i] += math.floor((left_quantity - now) / left_days)
        b[-1] += left_quantity - sum(b)
    return b


if __name__ == '__main__':
    w = list()
    quant = 220
    """for i in range(5, 15):
        w = distribution_by_days(quant, i)
        w.reverse()
        print(i, w, sum(w), sep=': ')"""
    s = '[4, 3, 4, 4, 7, 10, 10, 17, 18, 27, 48, 68]'
    print(regenerate_distribution(150, 2, s))
