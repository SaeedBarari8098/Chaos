import matplotlib
matplotlib.use("TkAgg")   # GUI backend
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
import numpy as np

# -------------------------
# Parameters for Lorenz system
# -------------------------
sigma = 10.0
beta = 8.0 / 3.0
rho = 28.0

# Initial conditions
init_1 = [1.0, 1.0, 1.0]
init_2 = [1.0001, 1.0, 1.0]

# Time
start, finish = 0, 100
time_step = 15000   # Reduced for smooth animation
t_eval = np.linspace(start, finish, time_step)
t_span = (start, finish)

# -------------------------
# Lorenz equations
# -------------------------
def lorenz_equations(t, loc, sigmas, betas, rhos):
    x, y, z = loc
    dx_dt = sigmas * (y - x)
    dy_dt = x * (rhos - z) - y
    dz_dt = x * y - betas * z
    return [dx_dt, dy_dt, dz_dt]

# Solve for both trajectories
ans1 = solve_ivp(lorenz_equations, t_span, init_1, args=(sigma, beta, rho), t_eval=t_eval, method='RK45')
ans2 = solve_ivp(lorenz_equations, t_span, init_2, args=(sigma, beta, rho), t_eval=t_eval, method='RK45')

x1, y1, z1 = ans1.y
x2, y2, z2 = ans2.y

# -------------------------
# Set up 3D figure
# -------------------------
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(min(np.min(x1), np.min(x2)), max(np.max(x1), np.max(x2)))
ax.set_ylim(min(np.min(y1), np.min(y2)), max(np.max(y1), np.max(y2)))
ax.set_zlim(min(np.min(z1), np.min(z2)), max(np.max(z1), np.max(z2)))
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Lorenz System (Chaotic Waterwheel Evolution)")

# -------------------------
# Initialize lines and points
# -------------------------
line1, = ax.plot([], [], [], lw=0.8, color="blue", label=f"Trajectory 1: {init_1}")
point1, = ax.plot([], [], [], 'o', color="red")

line2, = ax.plot([], [], [], lw=0.8, color="green", label=f"Trajectory 2: {init_2}")
point2, = ax.plot([], [], [], 'o', color="orange")

# -------------------------
# Initialization function
# -------------------------
def init():
    for artist in [line1, point1, line2, point2]:
        artist.set_data([], [])
        artist.set_3d_properties([])
    return line1, point1, line2, point2

# -------------------------
# Update function for animation
# -------------------------
def update(frame):
    # Update first trajectory
    line1.set_data(x1[:frame], y1[:frame])
    line1.set_3d_properties(z1[:frame])
    point1.set_data([x1[frame]], [y1[frame]])
    point1.set_3d_properties([z1[frame]])

    # Update second trajectory
    line2.set_data(x2[:frame], y2[:frame])
    line2.set_3d_properties(z2[:frame])
    point2.set_data([x2[frame]], [y2[frame]])
    point2.set_3d_properties([z2[frame]])

    return line1, point1, line2, point2

# -------------------------
# Create animation
# -------------------------
frames = len(t_eval) - 1  # avoid index error
ani = FuncAnimation(fig, update, frames=frames, init_func=init, interval=20, blit=False)

plt.legend()
plt.show()


fig = plt.figure(figsize=(14, 8))
# 3D plot of the Lorenz attractor
ax = fig.add_subplot(121, projection='3d')
ax.plot(x1, y1, z1, lw=0.7,
        label=f"({init_1[0]}, {init_1[1]}, {init_1[2]})",
        color = "blue")
ax.plot(x2, y2, z2, lw=0.7,
        label=f"({init_2[0]}, {init_2[1]}, {init_2[2]})",
        linestyle='dashed',color = "green")
ax.set_title("Lorenz System (Chaotic Waterwheel)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()

# Time series to highlight butterfly effect
ax2 = fig.add_subplot(122)
delta_r = np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)

ax2.plot(t_eval, delta_r, lw=1.2, color='red')
ax2.set_title("Divergence of Nearby Trajectories")
ax2.set_xlabel("Time")
ax2.set_ylabel("|r1 - r2|")
ax2.set_yscale('log')
plt.tight_layout()

ani = FuncAnimation(fig, update,
                    frames=frames,
                    init_func=init,
                    interval=20, blit=False)
plt.show()