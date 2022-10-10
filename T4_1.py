# 1. Вычислить число c заданной точностью d
#in
#Enter a real number: 9
#Enter the required accuracy '0.0001': 0.000001

#out
#9.000000

from decimal import Decimal


def acc(N, a):
    number = Decimal(f"{N}")
    return number.quantize(Decimal(f"{a}"))
print(acc(float(input("Enter a real number: ")), float(input("Enter the required acc 0.0001: "))))



