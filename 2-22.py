import matplotlib.pyplot as plt
n = [255, 127, 64, 32, 5, 0]
v = [3.228, 1.667, 0.865, 0.458, 0.117, 0.053]
plt.figure (figsize=(8,6), dpi=100)
plt.axis([0, 300, 0, 3.5])

plt.plot(n, v, "-0")
plt.legend()
plt.show()