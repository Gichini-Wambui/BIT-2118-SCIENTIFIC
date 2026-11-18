# Task 5: Matrix Algebra and Matrix Operations

*Programs:* `code/Task_05_matrix_algebra.py` (original) and `code/Task_05_modified.py` (parameter change + new case). Run from inside the `code/` folder.

## 1. Inputs and mathematical operation
Four square corners, a 45° rotation matrix, a scaling matrix diag(2, 1.5). Operations: matrix product (rotation @ scale), applying it to all points (`points @ T.T`), determinant.

## 2. Original output and its meaning
```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 2.9999999999999996
```
The unit square becomes a rotated parallelogram: (1,0) maps to (1.414, 1.414) and (0,1) to (−1.061, 1.061). The determinant 3.0 = 2 × 1.5 says areas are multiplied by 3 (rotation does not change area; scaling does). A positive determinant means orientation is preserved and the matrix is invertible.

## 3. Parameter change and how the result changes
With a 90° rotation and no scaling the square maps to (0,0),(0,1),(−1,1),(−1,0) with determinant 1 (area unchanged). With 45° and scale (2, 3) the determinant is 6, and a reflection diag(1, −1) has determinant −1 (orientation flipped).

## 4. Modified program: new real-world case
**Assumptions, inputs and data:** A robot gripper outline 0.4 m × 0.1 m must be rotated 30° and moved to position (2.0, 1.0) m. Homogeneous coordinates [x, y, 1] let rotation and translation be one 3×3 matrix.

**Output of `Task_05_modified.py`:**
```text
=== PART 1: Parameter changes ===
90 deg rotation, no scaling -> transformed points:
 [[ 0.  0.]
 [ 0.  1.]
 [-1.  1.]
 [-1.  0.]]
Determinant: 1.0 (area unchanged)

45 deg + scale (2, 3) determinant: 6.0 (area multiplied by 6)
Reflection determinant: -1.0 (negative = orientation flipped)

=== PART 2: Robot tool path with homogeneous coordinates ===
Homogeneous transform:
 [[ 0.866 -0.5    2.   ]
 [ 0.5    0.866  1.   ]
 [ 0.     0.     1.   ]]
Gripper corners in the workspace (m):
 [[2.     1.    ]
 [2.3464 1.2   ]
 [2.2964 1.2866]
 [1.95   1.0866]]
Determinant of the 2x2 rotation part: 1.0
Recovered original outline with H^-1: True
```
**Interpretation:** Transformed corners are listed in the output; the first corner lands exactly at (2.0, 1.0). The rotation part still has determinant 1 (shape unchanged). Multiplying by the inverse matrix recovers the original outline (`True`), demonstrating that matrix inverses undo transformations.

