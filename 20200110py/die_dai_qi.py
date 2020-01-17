from collections.abc import Iterable
from collections.abc import Iterator
print (isinstance([], Iterable))
print (isinstance({}, Iterable))
print (isinstance('abc', Iterable))
print (isinstance((x for x in range(10)), Iterable))
print (isinstance(100, Iterable))
a = isinstance((x for x in range(18)), Iterator)
b = isinstance([], Iterator)
print (a)
print (b)