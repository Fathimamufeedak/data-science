import numpy as np
import math

# (a) Translation matrix
def translation_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0,  1]
    ])

# (b) Rotation matrices
def rotation_matrix_x(theta_deg):
    theta = math.radians(theta_deg)
    return np.array([
        [1, 0,           0,          0],
        [0, math.cos(theta), -math.sin(theta), 0],
        [0, math.sin(theta),  math.cos(theta), 0],
        [0, 0,           0,          1]
    ])

def rotation_matrix_y(theta_deg):
    theta = math.radians(theta_deg)
    return np.array([
        [math.cos(theta), 0, math.sin(theta), 0],
        [0,               1, 0,               0],
        [-math.sin(theta), 0, math.cos(theta), 0],
        [0,               0, 0,               1]
    ])

def rotation_matrix_z(theta_deg):
    theta = math.radians(theta_deg)
    return np.array([
        [math.cos(theta), -math.sin(theta), 0, 0],
        [math.sin(theta),  math.cos(theta), 0, 0],
        [0,               0,                1, 0],
        [0,               0,                0, 1]
    ])

# (c) Scaling matrix
def scaling_matrix(sx, sy, sz):
    return np.array([
        [sx, 0,  0,  0],
        [0, sy,  0,  0],
        [0,  0, sz,  0],
        [0,  0,  0,  1]
    ])

# ---- Input from user ----
tx = float(input("Enter translation values tx, ty, tz: "))
ty = float(input())
tz = float(input())

theta_x = float(input("Enter rotation angle around X-axis (in degrees): "))
theta_y = float(input("Enter rotation angle around Y-axis (in degrees): "))
theta_z = float(input("Enter rotation angle around Z-axis (in degrees): "))

sx = float(input("Enter scaling values sx, sy, sz: "))
sy = float(input())
sz = float(input())

# ---- Generate Matrices ----
T = translation_matrix(tx, ty, tz)
Rx = rotation_matrix_x(theta_x)
Ry = rotation_matrix_y(theta_y)
Rz = rotation_matrix_z(theta_z)
S = scaling_matrix(sx, sy, sz)

# ---- Output ----
print("\nTranslation Matrix:")
print(T)

print("\nRotation Matrix about X-axis:")
print(Rx)

print("\nRotation Matrix about Y-axis:")
print(Ry)

print("\nRotation Matrix about Z-axis:")
print(Rz)

print("\nScaling Matrix:")
print(S)
