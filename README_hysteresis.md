# hysteresis.py

## Description: 
This Python script simulates the hysteresis behavior of a one-dimensional Ising spin chain using a zero-temperature Monte Carlo algorithm. It models spin interactions under an external magnetic field and visualizes the resulting magnetization loop. The code support four, five and six spins for natural and polar stack. 


## Required Version: 
This script was developed using Python 3.9.

## Usage:
1.	Set the number of spins in N_spins variable (4, 5, or 6) and choose the stacking type in the variable interface (‘polar’ or ‘natural’).
2.	The code will generate a hysteresis plot for the desired configuration. Run time is a few seconds.
3.	Carefully set the variable steps in the monte_carlo_hysteresis function, as it may not reach the required minimum.

## Sources:
This script requires the following Python packages that can be installed in a few minutes:
- NumPy: https://numpy.org/install
- Matplotlib: https://matplotlib.org

## Author: 
José D. Mella
