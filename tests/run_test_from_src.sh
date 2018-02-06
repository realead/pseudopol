export PYTHONPATH="${PYTHONPATH}:../.."

if [ "$1" = "rebuild" ]; then
    (cd .. && python setup.py build_ext --inplace --force)
fi;

sh run_unit_tests.sh "$2"
