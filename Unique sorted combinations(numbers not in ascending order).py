from itertools import product


a, b = list(map(int, input().split()))


def solution(a, b):
    col = []
    for i in range(a):
        col.append(str(i))
    num = ''.join(col)
    res = []
    for x in product(num, repeat=b):
        ok = 0
        y = ''.join(x)
        for check in range(a):
            if y.count(str(check)) > 1:
                ok += 1
                break
        if ok == 0:
            res.append(y)
    return res


res = solution(a, b)
for n in range(len(res)):
    ans = ''
    for k in range(b):
        if k != b-1:
            ans = ans + res[n][k] + ' '
        else:
            ans = ans + res[n][k]
    print(ans)