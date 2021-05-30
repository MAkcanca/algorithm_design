def karatsuba_multiplication(x, y):
    # Split the numbers into two parts
    x = str(x)
    y = str(y)
    a, b = int(x[:int(len(x)/2)]), int(x[int(len(x)/2):])
    c, d = int(y[:int(len(y)/2)]), int(y[int(len(y)/2):])
    # Compute a*c
    step_1 = a * c
    # Compute b*d
    step_2 = b * d
    # Compute (a+b) * (c+d)
    step_3 = (a+b) * (c+d)
    # Compute step_3 - step_2 - step_1
    step_4 = step_3 - step_2 - step_1
    # Compute (step_1 with 4 trailing zeroes) + (step_2) + (step_4 with 2 trailing zeroes)
    step_5 = (step_1 * 10000) + (step_2) + (step_4 * 100)
    return step_5

if __name__=='__main__':
    from timeit import Timer
    t = Timer("karatsuba_multiplication(5678,1234)", "from __main__ import karatsuba_multiplication")
    print(t.timeit())
    t = Timer("5678*1234")
    print(t.timeit())