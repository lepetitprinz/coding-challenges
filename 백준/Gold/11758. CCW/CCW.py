x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

d1 = x1*y2 + x2*y3 + x3*y1
d2 = x2*y1 + x3*y2 + x1*y3

result = d1 - d2
if result > 0:
    print(1)
elif result == 0:
    print(0)
else:
    print(-1)