#numpy is needed for tests:


pip install numpy


WRAPPER="/usr/bin/time -f \"peak_used_memory:%M(Kb)elapsed_user_time:%U(sec)\""
#WRAPPER="/usr/bin/time"

echo "testing cfind_max_subsum 10**9:"
#$WRAPPER python "performance/cfind_max_subsum.py" 1000000000

echo "testing cfind_max_subsum 10**4:"
$WRAPPER python "performance/cfind_max_subsum.py" 10000

echo "testing pfind_max_subsum 10**4:"
$WRAPPER python "performance/pfind_max_subsum.py" 10000

echo "testing pfind_max_subsum 10**8:"
$WRAPPER python "performance/pfind_max_subsum.py" 100000000
