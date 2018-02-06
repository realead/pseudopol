# pseudopol
a collection of algorithms for pseudo polynomial problems

## Installation

This module can be used by python2.7 and python3. The easiest way to install/test is to use virtual environment (here for python2.7):

    virtualenv -p python2.7 p27
    source p27/bin/activate
    (p27) ...

Right now cython-tool-chain is needed for installation:

    (p27)pip install cython

Now the current version can be installed from github:

    (p27) pip install https://github.com/realead/pseudopol/zipball/master

It is possible to uninstall it afterwards via

    (p27) pip uninstall pseudopol

You can also install using the setup.py file from the root directory of the project:

    (p27) python setup.py install

However, there is no easy way to deinstall it afterwards (only manually) if `setup.py` was used directly.

You could also use the module without installation, by augmenting the python-path via enviroment variable

    export PYTHONPATH="${PYTHONPATH}:<path_to_pseudopol>"

or programmatically, for example with help of

    import sys
    sys.path.append(path_to_exetest)


The same can be done for Python3.
