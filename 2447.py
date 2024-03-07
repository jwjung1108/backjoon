n = int(input())

arr = [["*"] * n for _ in range(n)]

print("\n".join(["".join([str(i) for i in row]) for row in arr]))
print("---------------------------------------------")


def star(n, before, arr):
    if n <= 1:
        return
    if n != before:
        # for i in range()





    for i in range(0, n):
        for k in range(0, n):
            if (i >= n / 3 and i < (n / 3) * 2) and (k >= n / 3 and k < (n / 3) * 2):
                arr[i][k] = " "
                continue
    star(n // 3, arr)
    return


star(n, n, arr)

print("\n".join(["".join([str(i) for i in row]) for row in arr]))
