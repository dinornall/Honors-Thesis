import matplotlib.pyplot as plt
from pyFAST.input_output import FASTOutputFile

# 1. Load the binary output file
# Make sure the filename matches what OpenFAST generated
df = FASTOutputFile('Main.outb').toDataFrame()

# 2. Extract the time and the data channels you want
time = df['Time_[s]']
tower_deflection = df['TTDspFA_[m]'] # Tower fore-aft displacement
blade_deflection = df['OoPDefl1_[m]'] # Blade 1 out-of-plane deflection

# 3. Plot the data
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax1.plot(time, tower_deflection, color='blue')
ax1.set_ylabel('Tower Deflection (m)')
ax1.set_title('NREL 5MW Structural Response')
ax1.grid(True)

ax2.plot(time, blade_deflection, color='green')
ax2.set_ylabel('Blade 1 Deflection (m)')
ax2.set_xlabel('Time (s)')
ax2.grid(True)

plt.tight_layout()
plt.show()