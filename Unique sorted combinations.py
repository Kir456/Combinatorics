from itertools import *

print('Write length of combinations and number up to which not including there will be numbers in combinations')
a, b = list(map(int, input().split()))
res = []


def solution(a, b):
    if a == 0:
        return
    num = ''
    for u in range(b):
        num += str(u)
    for i in product(num, repeat=a):
        ok = 0
        s = ''.join(i)
        add = []
        for t in range(b):
            if s.count(str(t)) > 1:
                ok = 1
                break
        if ok == 0:
            for n in range(a):
                add.append(int(s[n]))
            add = sorted(add)
            if add not in res:
                res.append(add)
    return res


if a == 0:
    print('No output')
else:
    solution(a, b)
    for j in range(len(res)):
        ans = ''
        line = (str(i) for i in res[j])
        count = 0
        for output in line:
            count += 1
            if count != a:
                ans = ans+output + ' '
            else:
                ans += output
        print(ans)