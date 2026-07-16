from typing import NamedTuple

class Point(NamedTuple):
    x: int 
    y: int

point = Point(10, 20)

print(point.x)  #more readable than point[0]
print(point.y)

# Dataclass	                 NamedTuple
# ----------------------------------------------
# Mutable by default	    Immutable
# Best for application 
# models	                Best for fixed records
# Can contain many 
# methods	                Usually lightweight