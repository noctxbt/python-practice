from math import sin, cos, tan, pi, radians

x = radians(float(input()))

sinx = sin(x)
cosx = cos(x)
tanx = tan(x) * tan(x)

res = sinx + cosx + tanx

print(res)
