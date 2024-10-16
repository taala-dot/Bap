def calculate(a, b, c):
    return (c // 2) * (a - b) + (c % 2) * a

t = int(input("Введите количество тестов: "))
while t > 0:
    a, b, c = map(int, input().split())
    print(calculate(a, b, c))
    t -= 1
