import numpy as np
import matplotlib.pyplot as plt

#If N_spins=5, use interface="polar" 
N_spins=6
#polar or natural
interface="polar"

# Compute the total energy of the spin configuration
def energy(spins, J, B):
    # Ising interaction energy between nearest neighbors
    if N_spins==4:
        interaction_energy = -(J[0]*spins[0]*spins[1] + J[1]*spins[1]*spins[2] + J[2]*spins[2]*spins[3])
        interaction_demag  = 0.0*np.sum(spins)**2
    if N_spins==5:
        if interface=="polar":
            interaction_energy = -(J[0]*spins[0]*spins[1] + J[1]*spins[1]*spins[2] + J[2]*spins[2]*spins[3] + J[3]*spins[3]*spins[4])
            interaction_demag  = 0.00002*np.sum(spins)**2
        else:
            print("Please use interface=polar")
    elif N_spins==6:
        interaction_energy = -(J[0]*spins[0]*spins[1] + J[1]*spins[1]*spins[2] + J[2]*spins[2]*spins[3] + J[3]*spins[3]*spins[4] + J[4]*spins[4]*spins[5])
        interaction_demag  = 0.0*np.sum(spins)**2
    
    # Magnetic energy: Zeeman term, where the factor 3 is related to the monolayer magnetization (see supplementary material)
    muB = 5.788e-5  # Bohr magneton in eV/T
    magnetic_energy = -3 * muB * B * np.sum(spins)
    
    return interaction_energy + magnetic_energy + interaction_demag

# Perform one Metropolis Monte Carlo step
def metropolis_step(spins, J, B):
    # Randomly select a spin to flip
    i = np.random.randint(0, len(spins))  
    new_spins = spins.copy()
    # Flip the spin
    new_spins[i] *= -1                    
    
    # Calculate energy difference
    dE = energy(new_spins, J, B) - energy(spins, J, B)
    
    # Accept the move if energy decreases (T=0, so no probabilistic acceptance)
    if dE < 0:
        spins[i] *= -1
    return spins

# Run the hysteresis loop by sweeping magnetic field B
def monte_carlo_hysteresis(steps, J, B_range,spin_inicial):
    spins = spin_inicial.copy()  # Use provided initial spin configuration
    hysteresis_data = []
    
    for B in B_range:
        # Perform multiple Monte Carlo steps at fixed B
        for k in range(steps):
            spins = metropolis_step(spins, J, B)
        
        # Record magnetization after relaxation
        magnetization = np.sum(spins)
        hysteresis_data.append((B, magnetization))

    return np.array(hysteresis_data)

# Simulation parameters
J0 = -0.000135
# Coupling constants for nearest neighbors
if N_spins==4:
    if interface=="natural":
        J = np.array([J0,J0,J0])
    elif interface=="polar":
        J = np.array([J0,-0.4*J0,J0])
if N_spins==5:
    if interface=="natural":
        J = np.array([J0,J0,J0,J0])
    elif interface=="polar":
        J = np.array([J0,J0,-0.4*J0,J0])    
elif N_spins==6:
    if interface=="natural":
        J = np.array([J0,J0,J0,J0,J0])
    elif interface=="polar":
        J = np.array([J0,J0,-0.4*J0,J0,J0])

# Magnetic field sweep range
B_values = np.linspace(-4, 4, 300)   # Increasing field
B_values2 = np.linspace(4, -4, 300)  # Decreasing field

# Initial spin configuration. S0 was set to 1 for simplicity (see Supplementary Material for details)
S0 = 1
if N_spins==4:
    initial_state = np.array([-S0,-S0,-S0,-S0])  
elif N_spins==5:
    initial_state = np.array([-S0,-S0,-S0,-S0,-S0])
elif N_spins==6:
    initial_state = np.array([-S0,-S0,-S0,-S0,-S0,-S0])
# Run hysteresis simulations for increasing and decreasing field
# 'steps' parameter should be chosen carefully due to the finite computational time.
hysteresis_data = monte_carlo_hysteresis(steps=3030, J=J, B_range=B_values, spin_inicial=initial_state)
hysteresis_data2 = monte_carlo_hysteresis(steps=3010, J=J, B_range=B_values2, spin_inicial=-initial_state)

# Plot the hysteresis loop
plt.figure(figsize=(7, 5))
plt.plot(B_values, hysteresis_data[:, 1], "--", label="Increasing")
plt.plot(B_values2, hysteresis_data2[:, 1], "-", label="Decreasing")
plt.xlabel("B (T)", fontsize=14)
plt.ylabel("Magnetization (arb. u.)", fontsize=14)
#plt.title("Hysteresis Loop of 4-Spin Ising Model, 2L+2L", fontsize=16)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
if N_spins==4:
    plt.ylim(-5, 5)
    plt.xlim(-2.5, 2.5)
elif N_spins==5:
    plt.ylim(-6, 6)
    plt.xlim(-3, 3)
elif N_spins==6:
    plt.ylim(-7, 7) 
    plt.xlim(-2.5, 2.5)

plt.grid()

# Uncomment to save the figure
plt.savefig("hysteresis.pdf")

# plt.show()
