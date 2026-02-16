Lorenz System Visualization and Chaotic Trajectories

This Python script simulates and visualizes the Lorenz system, a classic example of a chaotic system, often used to demonstrate the butterfly effect. The code computes two nearby trajectories and shows how small differences in initial conditions diverge over time.

Features

3D Lorenz Attractor Animation

Animates two trajectories in 3D space.

Shows trajectory points moving in real-time.

Highlights differences between two slightly different initial conditions.

Static 3D Plot

Plots both trajectories for full simulation.

Trajectories are color-coded and labeled by initial conditions.

Divergence Plot

Displays the time evolution of the distance between the two trajectories.

Uses logarithmic scale to emphasize exponential divergence (chaos).

Dependencies

This code requires the following Python packages:

numpy

matplotlib

scipy

Install dependencies via pip if you don’t already have them:

pip install numpy matplotlib scipy
Lorenz System

The Lorenz system is defined by the equations:

𝑥˙=𝜎(𝑦−𝑥)
𝑦˙=𝑥(𝜌−𝑧)−𝑦
𝑧˙=𝑥y−𝛽𝑧


Parameters in the code:

sigma = 10.0

beta = 8/3

rho = 28.0

Initial conditions:

Trajectory 1: [1.0, 1.0, 1.0]

Trajectory 2: [1.0001, 1.0, 1.0] (slightly different for butterfly effect)

How to Run

Save the script as lorenz_visualization.py.

Run it using Python:

python lorenz_visualization.py

Two plots will appear:

An animated 3D visualization of the trajectories.

A static figure showing:

3D trajectories of both initial conditions.

Logarithmic plot of trajectory divergence over time.

Code Structure

Parameter Setup

Sets Lorenz parameters and initial conditions.

Defines time range and resolution.

Lorenz Equations

Function lorenz_equations returns the derivatives [dx/dt, dy/dt, dz/dt].

Integration

Solves the Lorenz system using scipy.integrate.solve_ivp for both trajectories.

3D Animation

Uses matplotlib.animation.FuncAnimation.

Updates lines and points for each trajectory frame-by-frame.

Static Plots

3D trajectory plot.

Divergence plot highlighting sensitivity to initial conditions.

Visualization Notes

Animation Colors:

Trajectory 1: Blue line with red point.

Trajectory 2: Green line with orange point.

Static Plots:

Trajectory lines are color-coded (blue & green dashed).

Divergence plot shows |r1 - r2| on a logarithmic scale.

GUI Backend:

matplotlib.use("TkAgg") is used for interactive 3D plotting.

Ensure your Python environment supports Tkinter.

References

Lorenz, Edward N. “Deterministic Nonperiodic Flow.” Journal of the Atmospheric Sciences, 1963

Matplotlib 3D Animation Documentation

This script is ideal for exploring chaotic dynamics, the butterfly effect, and 3D visualization in Python.
