import ctypes
from ctypes import c_double, c_int, pointer, POINTER
import numpy as np

def load_function(dll_path, function_name, function_argtypes):
    dll = ctypes.CDLL(dll_path, mode=ctypes.RTLD_GLOBAL)
    func = dll.chi2
    func.argtypes = function_argtypes
    return func

chi2 = load_function('./_chi2.so', 'chi2', [
    c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int, POINTER(c_double)
])

if __name__ == '__main__':
    
    mu_y = 0.
    sig_y = 5.
    mu_x = 0.21
    sig_x = 3.

    N = int(1000)
    m = float(1.)
    b = float(0.)

    x = np.random.normal(mu_x, sig_x, N).astype('float64')
    x_p = x.ctypes.data_as(POINTER(c_double))
    y = np.random.normal(mu_y, sig_y, N).astype('float64')
    y_p = y.ctypes.data_as(POINTER(c_double))
    yerr = np.array([sig_y] * N, 'float64')
    yerr_p = yerr.ctypes.data_as(POINTER(c_double))
    result = c_double()
    result_p = pointer(result)

    chi2(m, b, x_p, y_p, yerr_p, N, result_p)
    print(result_p.contents)

