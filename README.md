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

## Functionality

There are two sets of functions:

   1. the pure python implementation, which can be found in module `pseudopol.ppseudopol`
   2. fast C-implementation which can be found in `pseudopol.cpseudopol`

### find_max_subsum

Given the values of objects `Oi` `i=1...n`, find a subsum `S=sum Oi` for `i` from `I` - a subset of `{1...n}` which is maximal and <= some given maximal value `max_val`.

Properties:

   1. c-version needs around 1bit times `max_val`, python version around 80bytes, i.e. 640 times more (actually unclear why)
   2. Time complexity `O(n*max_val)`, c-version is about 1000 times faster than the python version (bit-tricks possible).
   
### zerosum_subset_exists

Given the values of objects `Oi` `i=1...n`, find a non-empty subset where the sum of elements is `0`.


## Testing

The test scripts are in folder `tests`. Call

    sh run_test_from_src.sh rebuild N

for running all (unit) tests using the current sources. Skip rebuild if rebuild of the extensions isn't needed. `N` gives the number of random tests and can be simply omited.

Run 

    sh test_install.sh PYTHON_VERSION 

to create a new virtual environment, install cython and pseudopol from the source and run all unit tests using this installation. Choose `PYTHON_VERSION=p2` for python 2 or `p3` for python 3.

By calling 

    sh test_install.sh PYTHON_VERSION from-git

the installed `pseudopol` version isn't from the current source, but will be downloaded from the git-repository.

## History

0.1.0 `find_max_subsum`
0.2.0 `zerosum_subset_exists` // bug fixes 
