
export PYTHONPATH="${PYTHONPATH}:.."

if [ "$1" = "rebuild" ]; then
    (python setup.py build_ext --inplace --force)
fi;

(cd tests && python -m unittest discover -s . -v)

