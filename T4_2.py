# 2. Задайте натуральное число N. Напишите программу,
#    которая составит список простых множителей числа N.
#in
#54

#out
#[2, 3, 3, 3]

def find_nums(N):
    p_f = []
    di = 2
    while N > 1:
        if N % di == 0:
            p_f.append(di)
            N //= di
        else:
            di += 1
    return p_f
print(find_nums(int(input())))
