int chi2(double m, double b, double *x, double *y, double *yerr, int N, double* result) {
    int n;double diff;
    
    *result = 0.0; 

    for (n = 0; n < N; n++) {
        diff = (y[n] - (m * x[n] + b)) / yerr[n];
        *result += diff * diff;
    }

    return 0;
}
