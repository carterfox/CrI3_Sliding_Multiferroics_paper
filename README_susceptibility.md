# susceptibility.nb

## Description: 
This Mathematica script analyzes the symmetry properties of a symbolic rank-3 tensor χ<sub>ijk</sub> under a set of spatial symmetry operations associated with the CrI<sub>3</sub> point group. It identifies which tensor components remain nonzero after applying the symmetry constraints. If any nonzero components are found, the script displays them using a compact notation. The tensor for the point group m is the even part of the magnetic point group m’, then is not considered in the script.

## Required Version:

This script was developed using Mathematica 14.3.

## Usage: 
1.	The script contains the symmetry operations of the magnetic point group 2/m’ and m’ and non-magnetic point groups m. Comment or uncomment the corresponding sections in the script to examine the second-order susceptibility tensor of the desired point group.
2.	Run the script in Mathematica. Run time is a few seconds. 
3.	The output will show the nonzero components of the tensor χ<sub>ijk</sub> that satisfy all symmetry constraints.
4.	The outputs are written as: χ<sub>ijk</sub> → B<sub>αβγ</sub>, where B<sub>αβγ</sub> are constants that help identify which tensor components are equivalent. For example, if χ<sub>123</sub> → B<sub>123</sub> y χ<sub>132</sub> → B<sub>132</sub>, then χ<sub>123</sub> = χ<sub>132</sub>, meaning those tensor components are equal.

- Applicable to theoretical modeling in condensed matter physics and materials science.

## Sources:
The matrix representation of the symmetry operations were taken from the Bilbao crystallography Server: [Point Group Tables](http://webbdcrista2.ehu.es/cryst/mpoint_uni.html) 

## Author: 
José D. Mella
