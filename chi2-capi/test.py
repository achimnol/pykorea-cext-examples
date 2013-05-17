import numpy as np
from _chi2 import chi2

if __name__ == '__main__':
 
    mu_y = 0.
    sig_y = 5.
    mu_x = 0.21
    sig_x = 3.

    N = int(1000)
    m = float(1.)
    b = float(0.)

    x = np.random.normal(mu_x, sig_x, N).astype('float64')
    y = np.random.normal(mu_y, sig_y, N).astype('float64')
    yerr = np.array([sig_y] * N, 'float64')
    result = chi2(m, b, x, y, yerr)  # The module determines N from the arguments.
    print(result)

