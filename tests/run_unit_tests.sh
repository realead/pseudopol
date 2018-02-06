
export PYTHONPATH="${PYTHONPATH}:../.."

if [ "$1" = "rebuild" ]; then
    (cd .. && python setup.py build_ext --inplace --force)
fi;


### setting the number of random tests
export RTC_COUNT="$2"
(cd unit_tests && python -m unittest discover -s . -v)

