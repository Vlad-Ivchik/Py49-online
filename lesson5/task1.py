# a
import math

n_start = 0
n_end = 16

x = 10

value = 0.0

sin_x = math.sin(x)

for n in range(n_start, n_end):
    value += math.pow(-1, n) * ((math.pow(x, 2*n + 1)) / (math.factorial(2*n + 1)))


print(f"sin(x) = {sin_x}")
print(f"Sum: {value}")
print(f"Diff: {value - sin_x}")

print()
# b
import math

n_start = 0
n_end = 16

x = 10

value = 0.0

cos_x = math.cos(x)

for n in range(n_start, n_end):
    value += math.pow(-1, n) * ((math.pow(x, 2*n)) / (math.factorial(2*n)))


print(f"cos(x) = {cos_x}")
print(f"Sum: {value}")
print(f"Diff: {value - cos_x}")
