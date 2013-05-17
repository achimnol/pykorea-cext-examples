pykorea-cext-examples
=====================

A series of C API examples taken &amp; modified from http://dan.iel.fm/posts/python-c-extensions/ and  https://gist.github.com/beaylott/3313315

Requirements
------------
이 예제는 Ubuntu 12.04 64bit Server Edition, C Python 3.3.0 (개발용 header 파일 포함), NumPy 1.7 이상을 필요로 합니다.

chi2-capi
---------
 * 컴파일 방법 : `python3 setup.py build_ext --inplace`
 * 실행 방법 : `python3` 실행 후 `import _chi2`

chi2-ctypes
-----------
 * 컴파일 방법 : `python3 setup.py build_ext --inplace`
 * 테스트 방법 : `python3 chi2.py`

chi2-cython
-----------
 * TODO
