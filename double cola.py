def find_character(n):
    p = 0
    if n <= 5:
        if n == 1:
            return "Sheldon"
        elif n == 2:
            return "Leonard"
        elif n == 3:
            return "Penny"
        elif n == 4:
            return "Rajesh"
        elif n == 5:
            return "Howard"  
    while 5 * 2 ** p <= n:
        n -= 5 * 2 ** p
        p += 1
    res = n // (2 ** p)
    if res == 0:
        return "Sheldon"
    elif res == 1:
        return "Leonard"
    elif res == 2:
        return "Penny"
    elif res == 3:
        return "Rajesh"
    else:
        return "Howard"
n = int(input("Введите число: "))
print(find_character(n))
