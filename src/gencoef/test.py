import numpy as np
import math

p = np.poly1d([
+0.1429511242e-53,
+0.1561712123e-44,
-0.2259472298e-35,
-0.2669710222e-26,
+0.9784247973e-18,
+0.1655572013e-8,
+0.3991098106e+0,
])
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

for i in range(1000):
  k = float(i) / 100
  print(sigmoid(k), p(k))
