"""Task 5 (modified): matrix algebra.
PART 1 - parameter change: rotate 90 deg and scale (1, 1); then a reflection (det < 0).
PART 2 - new case: robot arm tool - rotate 30 deg and translate, using homogeneous 3x3 matrices."""
import numpy as np

square = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])

def rot(deg):
    a = np.deg2rad(deg)
    return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])

print("=== PART 1: Parameter changes ===")
T1 = rot(90) @ np.diag([1.0, 1.0])
print("90 deg rotation, no scaling -> transformed points:\n", np.round(square @ T1.T, 3))
print("Determinant:", round(np.linalg.det(T1), 3), "(area unchanged)")
T2 = rot(45) @ np.diag([2.0, 3.0])
print("\n45 deg + scale (2, 3) determinant:", round(np.linalg.det(T2), 3), "(area multiplied by 6)")
T3 = np.diag([1.0, -1.0])                 # mirror about the x-axis
print("Reflection determinant:", round(np.linalg.det(T3), 3), "(negative = orientation flipped)")

print("\n=== PART 2: Robot tool path with homogeneous coordinates ===")
tool = np.array([[0., 0.], [0.4, 0.], [0.4, 0.1], [0., 0.1]])   # gripper outline (m)
tool_h = np.hstack([tool, np.ones((4, 1))])                      # add 1 -> [x, y, 1]
theta = np.deg2rad(30)
H = np.array([[np.cos(theta), -np.sin(theta), 2.0],              # rotate 30 deg, move to (2.0, 1.0)
              [np.sin(theta),  np.cos(theta), 1.0],
              [0, 0, 1]])
moved = tool_h @ H.T
print("Homogeneous transform:\n", np.round(H, 4))
print("Gripper corners in the workspace (m):\n", np.round(moved[:, :2], 4))
print("Determinant of the 2x2 rotation part:", round(np.linalg.det(H[:2, :2]), 6))
back = moved @ np.linalg.inv(H).T                                # undo the move with the inverse
print("Recovered original outline with H^-1:", np.allclose(back[:, :2], tool))
