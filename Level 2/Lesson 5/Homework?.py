# def palindrone(x):
#     print(x)
#     if len(x) <= 1:
#         return True
#     if x[0] != x[-1]:
#         return False
#     elif x[0] == x[-1]:
#         return palindrone(x[1:-1])
#
# print(palindrone("mom"))


def GCD(x, y, z):
    if y == 0:
        return x
    if x == 0:
        return y
    if x % z == 0 and y % z == 0:
        return z
    else:
        return GCD(x, y, z - 1)


def get_GCD(x, y):  # Use one-time helper function to start out recursion
    return GCD(x, y, min(x, y))  # (This temporarily sets it as the minimum but lets it be changeable)


print(get_GCD(600, 750))
