from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import warnings


#for the time being only with cython:
USE_CYTHON = True



extensions = Extension(
            name='pseudopol.cpseudopol',
            sources = ["pseudopol/cpseudopol.pyx"],
    )

if USE_CYTHON:
    extensions = cythonize(extensions)

kwargs = {
      'name':'pseudopol',
      'version':'0.2.0',
      'description':'Collection of solution for pseudo-polynomial problems',
      'author':'Egor Dranischnikow',
      'url':'https://github.com/realead/pseudopol',
      'packages':find_packages(),
      'license': 'MIT',
      'ext_modules':  extensions
}

try:
    setup(**kwargs)
except SystemExit:
    del kwargs['ext_modules']
    warnings.warn('compilation failed. Installing pure python package')
setup(**kwargs)


