import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import sympy as sp

def ba(vector_b, thetat):
    R = sp.Matrix([[sp.cos(thetat), sp.sin(thetat)],
                   [-sp.sin(thetat),  sp.cos(thetat)]])
    vector_a = R * vector_b
    return vector_a

t = sp.symbols('t')

# Set up symbolic variables
h1, l1, mnt, g, Jmt = sp.symbols('h1 l1 mnt g Jmt')
thetat = sp.Function('thetat')(t)

# Define dthetat for simplification
dthetat = sp.diff(thetat, t)

#Position vector
r_nt = sp.Matrix(ba(h1/2, thetat))
#Velocity vector
v_nt = r_nt.diff(t)

# Find Kinetic Energy
KE = 1/2*(Jmt)*dthetat**2
#Find Potential Energy
PE = mnt * g * (h1/2) * (-sp.cos(thetat))

# Lagrangian
L = KE - PE

eom = sp.simplify(sp.diff(sp.diff(L, dthetat), t) - sp.diff(L, thetat))
print("Original Symbolic EOM:")

# Substitute numerical values
numerical_vals = {
    mnt: 2.0,   # kg
    g: 9.81,    # m/s^2
    h1: 0.5,    # m
    Jmt: 0.1    # kg*m^2
}
eom = eom.subs(numerical_vals)
sp.pprint(eom)
print("-" * 30)

#Graphing

# chat's solution I don't do
# g = 9.81  # gravitational acceleration (m/s^2)

# # Nacelle parameters
# m_nt = 1.0  # mass of nacelle (kg)
# l_nt = 1  # width of nacelle (m)
# h_nt = 0.4  # height of nacelle (m)
# I_nt = (m_nt/12) * (l_nt**2 + h_nt**2) + m_nt*(h_nt/2)**2  # using parallel axis theorem
# thetat0 = np.pi/2  # initial angle (radians)
# thetat_dot0 = 0.0  # initial angular velocity (rad/s)

# def dynamics(t, y):
#     thetat, thetat_dot = y  # unpack the state vector into angle and angular velocity
#     # Equation of motion: I * theta_ddot + m * g * h_com * sin(theta) = 0
#     thetat_ddot = - ((m_nt * g * (h_nt/2)) / I_nt) * np.sin(thetat)  # calculate angular acceleration
#     return [thetat_dot, thetat_ddot]  # return the derivatives of the state vector

# # initial conditions and simulation
# y0 = [thetat0, thetat_dot0]  # set initial conditions for angle and angular velocity
# print(y0)  # print initial conditions
# t_final = 10.0  # set the final time for the simulation
# t_eval = np.linspace(0, t_final, 1000)  # create an array of time points for evaluation
# sol = solve_ivp(dynamics, (0, t_final), y0, t_eval=t_eval, rtol=1e-9, atol=1e-12)  # solve the ODE

# # Energies (time series)
# T = 0.5 * I_nt * sol.y[1]**2                       # kinetic energy
# V = m_nt * g * (h_nt/2) * (1 - np.cos(sol.y[0]))     # potential energy (zero at theta=0)                                        # total energy

# # Plots
# plt.figure()
# plt.plot(sol.t, sol.y[0], label='theta (rad)')
# plt.plot(sol.t, sol.y[1], label='theta_dot (rad/s)')
# plt.xlabel('Time (s)')
# plt.legend()
# plt.grid()
# plt.show()

   