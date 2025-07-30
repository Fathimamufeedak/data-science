import numpy as np
import math

# (a) Translation matrix
def translation_matrix(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

# (b) Rotation matrix (angle in degrees)
def rotation_matrix(theta_deg):
    theta_rad = math.radians(theta_deg)
    cos_t = math.cos(theta_rad)
    sin_t = math.sin(theta_rad)
    return np.array([
        [cos_t, -sin_t, 0],
        [sin_t,  cos_t, 0],
        [0,      0,     1]
    ])

# (c) Scaling matrix
def scaling_matrix(sx, sy):
    return np.array([
        [sx, 0,  0],
        [0, sy,  0],
        [0,  0,  1]
    ])

# --- Input from user ---
tx = float(input("Enter translation values tx and ty: "))
ty = float(input())
theta = float(input("Enter rotation angle (degrees): "))
sx = float(input("Enter scaling values sx and sy: "))
sy = float(input())

# Create matrices
T = translation_matrix(tx, ty)
R = rotation_matrix(theta)
S = scaling_matrix(sx, sy)

# --- Output ---
print("\nTranslation Matrix:")
print(T)

print("\nRotation Matrix:")
print(R)

print("\nScaling Matrix:")
print(S)
