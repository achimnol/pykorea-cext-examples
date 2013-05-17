from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

ext_modules=[
    Extension("chi2", ["chi2.pyx", "chi2_impl.c"]),
]

setup(
  name = "chi2",
  cmdclass = {"build_ext": build_ext},
  include_dirs = [np.get_include()],
  ext_modules = ext_modules
)
