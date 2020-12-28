README.txt

*********************************************************************************
# Python script for MLiC results verification usage.
# Necessary environments:
# Python3

*********************************************************************************
Preparing:
The cBench_V1.1.tar is download from https://sourceforge.net/projects/cbenchmark/files/cBench/V1.1/. More details about the benchmark and its usage can be found in this website or the file README-cBench-V1.1.txt.

NOTE that some programs have several bugs needing to be fixed and you might refer to our revised version in path ./data/compiled.tar.gz. All verifications are targeting the database 1 (MiDataSets) provided by cBench.

*********************************************************************************
Usage:
Unzip cBench_V1.1.zip before your running.

# Run verification for a specific program in your terminal:
cd yourpath/MLiCTestCodes
sudo Python3 MLiC_runs.py --app=automotive_susan_c

Reference output results after compilation and evaluation:
**********************************************
Application: automotive_susan_c, speedup: ***.
Execution time: -O3: *.*** sec, MLiC: *.*** sec.
**********************************************

We have completed evaluations of each single program on an Intel CPU platform, i7-3630QM@2.4GHz, runing VirtualBoxVM Linux 16.04 OS (single core). And you can find the raw records in file ./data/raw_records.txt. But as well-known, these optimizations are highly depended on the computation platform.

# Run for all programs:
cd Path-to-MLiC-verification
sudo Python3 MLiC_runs.py --app=ALL
*********************************************************************************
