#!/bin/sh

python2 -O Stress_Balls.py --no-plot 2>&1 | tee Stress_Balls_results.txt
python2 -O Stress_Balls.py --no-plot --reverse 2>&1 | tee -a Stress_Balls_results.txt

python3 -O Stress_Balls.py --no-plot 2>&1 | tee -a Stress_Balls_results.txt
python3 -O Stress_Balls.py --no-plot --reverse 2>&1 | tee -a Stress_Balls_results.txt
