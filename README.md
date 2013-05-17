pykorea-cext-examples
=====================

A series of C API examples taken &amp; modified from http://dan.iel.fm/posts/python-c-extensions/ and  https://gist.github.com/beaylott/3313315

Requirements
------------
이 예제는 Ubuntu 12.04 64bit Server Edition, C Python 3.3.0 (개발용 header
파일 포함), NumPy 1.7, Cython 0.19.1, CFFI 0.6 환경에서 테스트하였습니다.
NumPy, Cython, CFFI 모두 pip를 이용해 설치하실 수 있습니다.

chi2-capi
---------
 * 컴파일 방법 : `python3 setup.py build_ext --inplace`
 * 테스트 방법 : `python3 test.py`

chi2-ctypes
-----------
 * 컴파일 방법 : `python3 setup.py build_ext --inplace`
 * 테스트 방법 : `python3 test.py`

chi2-cython
-----------
 * 컴파일 방법 : `python3 setup.py build_ext --inplace`
 * 테스트 방법 : `python3 test.py`

chi2-cffi
-----------
 * 컴파일 방법 : `python3 setup.py build_ext --inplace`
 * 테스트 방법 : `python3 test.py`
