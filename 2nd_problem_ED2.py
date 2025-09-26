import numpy as np
import matplotlib.pyplot as plt


betas = [0.01, 0.5, 0.9999]
c = 1.0  # natural units, c=1


fig, axes = plt.subplots(1, 3, figsize=(15,5))

for ax, beta in zip(axes, betas):
    phi = np.arctanh(beta)

    R = np.array([[np.cos(phi), -np.sin(phi)],
                  [np.sin(phi),  np.cos(phi)]])
 e_x  = np.array([1, 0])
    e_ct = np.array([0, 1])

    e_xp  = R @ e_x
    e_ctp = R @ e_ct

    ax.axhline(0, color='black')  # x-axis
    ax.axvline(0, color='black')  # ct-axis

    
    scale = 1.0
    ax.plot([0, scale*e_xp[0]], [0, scale*e_xp[1]], 'r--', label="x'")
    ax.plot([0, scale*e_ctp[0]], [0, scale*e_ctp[1]], 'b--', label="ct'")
 ax.set_title(f"Lorentz boost with β = {beta}\nφ = {phi:.3f}")
    ax.set_xlabel("x")
    ax.set_ylabel("ct")
    ax.set_aspect('equal')
    ax.legend()
    ax.grid(True, ls=":")

plt.tight_layout()
plt.show()
