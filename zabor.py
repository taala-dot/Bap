def min_sum(n, k, s):
    for i in range(1, n + 1):
        s[i] += s[i - 1]
    ans = 0
    for j in range(1, n - k + 1):
        if s[ans + k] - s[ans] > s[j + k] - s[j]:
            ans = j

    return ans + 1

n, k = map(int, input("Введите n и k: ").split())
s = [0] + list(map(int, input("Введите массив s s: ").split()))

print(min_sum(n, k, s))

 