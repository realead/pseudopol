

echo "cnt: $1"
### setting the number of random tests
export RTC_COUNT="$1"
(cd unit_tests && python -m unittest discover -s . -v)

