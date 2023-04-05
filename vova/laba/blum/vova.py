def code(num,num1,num2):
    n = int(num)*int(num1)
    x_0 = (int(num2)*int(num2)) % n
    k = int(num) + int(num1)
    x = (x_0 * x_0) % n
    b = []
    b.append(x % 2)
    for i in range(k - 1):
        x = (x * x) % n
        b.append(x % 2)
    return b
