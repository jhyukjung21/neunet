# -----------------------------------------------------------
# Python:  3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18)
# [Clang 6.0 (clang-600.0.57)]
# Numpy:  1.18.2
# Matplotlib:  3.2.1
# -----------------------------------------------------------

inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output)
