import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# # Basic Plotting
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [2, 5, 1, 7, 9, 3, 6, 10]

# x = np.array(x)
# y = np.array(y)

# plt.plot(x, y, 'bo')
# plt.plot(x, 2*x + 5, 'r')
# plt.show()


# Last Square Regression
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [2, 5, 1, 7, 9, 3, 6, 10]

# x = np.array(x)
# y = np.array(y)

# A = np.vstack([x, np.ones(len(x))]).T
# y = y[:, np.newaxis]

# print(A)
# print(y)

# alpha = np.dot(np.dot(np.linalg.inv(np.dot(A.T, A)), A.T), y)
# print(alpha)

# plt.plot(x, y, 'bo')
# plt.plot(x, alpha[0]*x + alpha[1], 'r')
# plt.show()


# # Polynomial Regression
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [2, 5, 1, 7, 9, 3, 6, 10]

# x = np.array(x)
# y = np.array(y)

# for i in range (1, 7):
#     plt.subplot(2, 3, i)
#     plt.plot(x, y, 'bo')
    
#     y_est = np.polyfit(x, y, i)
#     print(y_est)
#     print(np.polyval(y_est, x))
#     print()
#     plt.plot(x, np.polyval(y_est, x), 'r')
    
# plt.show()

#cubic Interpolation
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 5, 1, 7, 9, 3, 6, 10]

x = np.array(x)
y = np.array(y)

f = CubicSpline(x, y)
x_new = np.linspace(1, 8, 100)
y_new = f(x_new)

plt.plot(x, y, 'bo')
plt.plot(x_new, y_new, 'r')
plt.show()