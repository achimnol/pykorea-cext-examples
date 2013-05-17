import numpy as np
cimport numpy as np

cdef extern from "chi2.h":
    int _chi2(double m, double b, double *x, double *y, double *yerr, int N)

def chi2(m, b,
         np.ndarray[np.double_t,ndim=1] x,
         np.ndarray[np.double_t,ndim=1] y,
         np.ndarray[np.double_t,ndim=1] yerr,
         N):
    cdef double result
    result = _chi2(m, b, <double*>x.data, <double*>y.data, <double*>yerr.data, N)
    return result
