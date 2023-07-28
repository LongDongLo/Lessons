def binConvert(x):
    x = bin(x)
    x = x[2:]
    counter = 0
    for i in x:
        if i == "1":
            counter = counter + 1
    return int(x), counter

print(binConvert(5))
