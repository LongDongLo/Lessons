# Homework: Vincent has 10 meters of fence material and needs to build a backyard fence.
# The backyard fence only has 3 sides because one side is his house.
# The backyard fence should form a rectangle with the side of the house.
# Length and width of the backyard fence can be different.
# Determine the length and width of his backyard that
# will give me the max area with his limited fence material.

# Homework: Vincent has 10 meters of fence material and needs to build a backyard fence.
# The backyard fence only has 3 sides because one side is his house.
# The backyard fence should form a rectangle with the side of the house.
# Length and width of the backyard fence can be different.
# Determine the length and width of his backyard that
# will give me the max area with his limited fence material.

maxA = 0
maxB = 0
maxArea = 0

for i in range(50):
    a = i/10
    b = 10-a*2
    area = a*b
    if area > maxArea:
        maxArea = area
        maxA = a
        maxB = b
    print("a =", a, "b =", b, "area =", area)
    print()

print("Max a =", maxA, "Max b =", maxB, "Max area =", maxArea)


