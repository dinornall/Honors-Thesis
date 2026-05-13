import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# --- 0. DEFINE STATE-SPACE FUNCTION ---
# This function computes the state-space representation of the 3-DOF wind turbine model.
def statespace(t, x, p):
    # t (float): Current time.
    # x (np.array): State vector [xn, psi, xb, xn_dot, psi_dot, xb_dot].
    # p (dict): Dictionary of model parameters.
    # np.array: The derivative of the state vector, x_dot.

    # Unpack the state vector for clarity
    xn, psi, xb, xn_dot, psi_dot, xb_dot = x

    # Unpack parameters from the dictionary
    M11, M22, M33 = p['M11'], p['M22'], p['M33']
    c_t, c_b = p['c_t'], p['c_b']
    k_t, k_b = p['k_t'], p['k_b']
    m_b, g, r_cg = p['m_b'], p['g'], p['r_cg']

    # --- External Forces (set to zero for this simulation) ---
    Fa_x = 0.0  # Aerodynamic thrust on the tower
    Qa   = 0.0  # Aerodynamic torque
    Qg   = 0.0  # Generator torque
    Qa_b = 0.0  # Generalized aerodynamic force on the blade

    # --- Calculate accelerations from the Equations of Motion ---
    xn_ddot = (Fa_x - c_t * xn_dot - k_t * xn) / M11
    psi_ddot = (Qa - Qg - m_b * g * r_cg * np.cos(psi)) / M22
    xb_ddot = (Qa_b - c_b * xb_dot - k_b * xb) / M33

    # --- Assemble the state derivative vector, x_dot ---
    return np.array([xn_dot, psi_dot, xb_dot, xn_ddot, psi_ddot, xb_ddot])

# --- 1. SETUP SIMULATION ---
# Create the parameter dictionary with placeholder values
p = {
    'M11': 6.0e6,    # Total effective mass for tower FA [kg]
    'M22': 5.0e7,    # Total rotational inertia [kg*m^2]
    'M33': 3.0e5,    # Blade generalized mass [kg]
    'c_t': 1.0e5,    # Tower damping [N/(m/s)]
    'c_b': 5.0e3,    # Blade damping [N/(m/s)]
    'k_t': 8.0e6,    # Tower stiffness [N/m]
    'k_b': 1.2e6,    # Blade stiffness [N/m]
    'm_b': 1.5e5,    # Blade mass [kg]
    'g': 9.81,       # Gravity [m/s^2]
    'r_cg': 45.0,    # Blade center of mass [m]
}