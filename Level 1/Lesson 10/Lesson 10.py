# import the library
import random
# can print numbers from 1-3
print(random.randint(1, 3))
print()

# can print numbers from 1-2
print(random.randrange(1, 3))
print()

# can print any rational number from 0-1
print(random.random())
print()

# can shuffle any list
list = [1, 2, 3]
random.shuffle(list)
print(list)
print()

# gives k amount of samples from given list
list = [1, 2, 3]
print(random.sample(list, k=2))
