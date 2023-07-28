"""
Data Structure #4: Data Sets

Data sets have no order, and no duplicates
The elements of a set are unchangeable, bu the set is
Sets will automatically ignore duplicate elements
You can store tuples but not lists in sets

You can make a consecutive set with set = set(range(1, 11))

Elements are outputted in random order
Numbers only sets are printed least to greatest

Add with set.add("element")
Add multiple with set.update(["a", "b"])

Remove using set.remove(element)
Remove without potential error with set.discard(element)
Take out the smallest/random element and return it with x = set.pop()
Clear sets with set.clear()

Check if sets are subsets with aSet.issubset(bSet)  # Will return true or false
Opposite is superset with aSet.issuperset(bSet)

Unions are all the unique elements in either set
aSet.union(bSet, cSet)

Intersection is the common elements between sets
aSet.intersection(bSet, cSet)

Disjoint returns true if theres is no in common intersection
aSet.isdisjoint(bSet)

Intersection update updates aSet to the intersections
aSet.intersection_update(bSet)

Relative difference subtracts the terms present in the other set as well
aSet.difference(bSet)
aSet.difference_update(aSet) # updates aSet to difference

Symmetric difference takes all the values only present in one set
aSet.symmetric_difference(bSet)
aSet.symmetric_difference_update(bSet)
"""

aSet = {1,2,3}
bSet = {2,3,4}
newAset = aSet.difference(bSet)
print(aSet.difference(newAset))

unionSet = aSet.union(bSet)
subSet = aSet.intersection(bSet)
print(unionSet.difference(subSet))
