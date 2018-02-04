from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules=cythonize(Extension(
            name='cpseudopol',
            sources = ["cpseudopol.pyx"],
    )))