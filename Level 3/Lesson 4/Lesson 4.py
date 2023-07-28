megalist = []
maxA = 0
maxB = 0
maxVolume = 0

for i in range(30):
    a = i/10 + 3
    b = (45-a**2)/(4*a)
    volume = a**2*b
    if volume > maxVolume:
        maxVolume = volume
        maxA = a
        maxB = b
    print("a =", a, "b =", b, "volume =", volume)
    print()

print("a =", maxA, "b =", maxB, "volume =", maxVolume)
