# electric_dipole.py

## Description: 
This Python script simulates the magnetic hysteresis behavior of a multiferroic under an external electric field. It models the evolution of polarization and magnetization using a numerical minimizator of the free energy. The simulation captures both forward and backward electric field sweeps and visualizes the resulting hysteresis loops for polarization and magnetization.

## Required Version: 
This script was developed using Python 3.9.

## Usage:
1.	Run the script directly to simulate the electric field sweep and compute equilibrium polarization and magnetization. Run time is a few seconds. 
2.	This code will generate three plots:
-	Free_energy.pdf : Free energy as a function of polarization at zero field.
-	Dipole.pdf : Electric polarization vs electric field.
-	Magnetization.pdf : Magnetization vs electric field.
3.	You can modify the sweep range or energy parameters inside the script to explore different regimes.

## Sources:
This script requires the following Python packages that can be installed in a few minutes:
- NumPy: https://numpy.org/install
- Matplotlib: https://matplotlib.org
- SciPy: https://scipy.org/install

## Author: 
José D. Mella
