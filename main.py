import math

a = float(input("Введіть  a: "))
b = float(input("Введіть  b: "))
eps = float(input("Введіть  ε: "))
m = 10

def f(x):
    return math.log(1 + 3*x)

def taylor_ln(x, eps):
    n = 1
    y = x
    term = x
    while abs(term) > eps:
        n += 1
        term *= -x * (n - 1) / n
        y += term
    return y

def calculate_f_values(a, b, eps, m):
    h = (b - a) / (m - 1)
    x = a
    print(" x    | math.log(1+3*x) | taylor_ln(1+3*x, eps) | eps        | iterations")
    print("------+----------------+-----------------------+------------+----------")
    for i in range(m):
        math_val = f(x)
        taylor_val = taylor_ln(3*x, eps)
        iteration_count = 0
        while abs(taylor_val - math_val) > eps:
            taylor_val = taylor_ln(3*x, eps)
            iteration_count += 1
        print(f"{x:.2f} | {math_val:.8f}   | {taylor_val:.8f}          | {eps:.2e} | {iteration_count}")
        x += h

calculate_f_values(a, b, eps , m)