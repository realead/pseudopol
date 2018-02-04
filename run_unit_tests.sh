
export PYTHONPATH="${PYTHONPATH}:.."

if [ "$1" = "rebuild" ]; then
    (cd pseudopol && python setup.py build_ext --inplace --force)
fi;

(cd tests && python -m unittest discover -s . -v)

