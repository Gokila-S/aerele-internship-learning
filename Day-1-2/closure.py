def multiplier(x):
    def multiply(y):
        return x * y
    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))