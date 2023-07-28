import autopy
import time
time.sleep(3)

def moveMouse(start,end):
    for i in range(2):
        if i == 0:
            condition = start
        elif i == 1:
            condition = end
        if condition == "a":
            autopy.mouse.move(600,550)
            time.sleep(0.07)
            autopy.mouse.click()
            time.sleep(0.07)
        elif condition == "b":
            autopy.mouse.move(800,550)
            time.sleep(0.07)
            autopy.mouse.click()
            time.sleep(0.07)
        elif condition == "c":
            autopy.mouse.move(1000,550)
            time.sleep(0.07)
            autopy.mouse.click()
            time.sleep(0.07)


def recursive(n, source, dest, aux):
    if n == 1:
        moveMouse(source, dest)
        return
    recursive(n-1, source, aux, dest)
    moveMouse(source, dest)
    recursive(n-1, aux, dest, source)


# def recursive(n, source, dest, aux):
#     if n == 1:
#         print("move disk from", source, "to", dest)
#     recursive(n-1, source, aux, dest)
#     print("move disk from", source, "to", dest)
#     recursive(n-1, aux, dest, source)

recursive(3,"a","c","b")
