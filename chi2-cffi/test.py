from cffi import FFI
from ctypes import c_double, c_int, pointer, POINTER
import numpy as np

ffi = FFI()
chi2 = ffi.dlopen('./_chi2.so')
ffi.cdef("""
int chi2(double m, double b, double *x, double *y, double *yerr, int N, double* result);
""")

if __name__ == '__main__':
    
    mu_y = 0.
    sig_y = 5.
    mu_x = 0.21
    sig_x = 3.

    N = int(1000)
    m = float(1.)
    b = float(0.)

    x = np.random.normal(mu_x, sig_x, N).astype('float64')
    x_p = ffi.cast('double *', x.ctypes.data)
    y = np.random.normal(mu_y, sig_y, N).astype('float64')
    y_p = ffi.cast('double *', y.ctypes.data)
    yerr = np.array([sig_y] * N, 'float64')
    yerr_p = ffi.cast('double *', yerr.ctypes.data)
    result = ffi.new('double *')

    chi2.chi2(m, b, x_p, y_p, yerr_p, N, result)
    print(result[0])

