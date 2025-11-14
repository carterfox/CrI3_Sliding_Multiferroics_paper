from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np

# Define the free energy as a function of polarization (x) and electric field (E)
def Free(x, E):
    P0 = 0.3  # Reference polarization value
    P1 = x    # Polarization variable
    return 5500 * (P1**4 - 2 * (P0**2) * (P1**2)) - 550 * E * P1

# Define magnetization as a linear function of polarization
def M(P):
    return 0.144 * P

# Create electric field sweep arrays (forward and backward)
E_up = np.linspace(-0.5, 0.5, 2000)
E_down = np.linspace(0.5, -0.5, 2000)

# Evaluate free energy at zero field for a range of polarization values
P = np.linspace(-0.5, 0.5, 100)
energy = [Free(p, 0) for p in P]

# Plot the free energy landscape
plt.figure()
plt.plot(P, energy)
plt.ylim(-50, 50)
plt.xlim(-0.6, 0.6)
plt.axhline(y=-45, color='r', linestyle='--')
plt.xlabel("Electric Polarization")
plt.ylabel("Free Energy")
plt.grid()
plt.savefig("free_energy.pdf")

# Initialize polarization and compute equilibrium polarization for increasing field
x0 = -0.5
p_up = []
for E in E_up:
    result = minimize(Free, x0, args=(E,))
    x0 = result.x
    p_up.append(x0)

# Repeat for decreasing field
p_down = []
for E in E_down:
    result = minimize(Free, x0, args=(E,))
    x0 = result.x
    p_down.append(x0)

# Plot polarization vs. electric field
plt.figure()
plt.plot(E_up, p_up, "r-")
plt.plot(E_down, p_down, "b-")
plt.xlabel("Electric Field")
plt.ylabel("Electric Polarization")
plt.xlim(-0.4, 0.4)
plt.grid()
plt.savefig("dipole.pdf")

# Compute magnetization from polarization
mag_up = [M(p[0]) for p in p_up]
mag_down = [M(p[0]) for p in p_down]

# Plot magnetization vs. electric field
plt.figure()
plt.plot(E_up, mag_up, "r")
plt.plot(E_down, mag_down)
plt.xlabel("Electric Field")
plt.ylabel("Magnetization")
plt.xlim(-0.4, 0.4)
plt.grid()
plt.savefig("magnetization.pdf")

