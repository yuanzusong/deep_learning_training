import numpy as np


def naive_relu(x):
    assert len(x.shape) == 2

    x = x.copy()
    print(x.shape[0])
    print('---------')
    print(x.shape[1])
    print('---------')
    for i in range(2):

        for j in range(4):

            x[i,j] = max(x[i,j], 0)

            print(x[i,j])
    return x

x = ([[1,2,3,4],
      [1,2,3,4]])

x = np.array(x)

# x.ndim
#
# print(x.ndim)
#
#
naive_relu(x)
print('----------')
print(x)
