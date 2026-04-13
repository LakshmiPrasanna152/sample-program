"""
============================================================
  COMPREHENSIVE NUMPY GUIDE
  Covers: numpy module, random module, broadcasting
============================================================
"""

import numpy as np
import numpy.random as npr

# ─────────────────────────────────────────────────────────
# 1. ARRAY CREATION
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("1. ARRAY CREATION")
print("="*50)

a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([[1, 2, 3], [4, 5, 6]])           # 2D array
a3 = np.zeros((3, 3))                             # all zeros
a4 = np.ones((2, 4))                              # all ones
a5 = np.full((3, 3), 7)                           # filled with 7
a6 = np.eye(4)                                    # identity matrix
a7 = np.arange(0, 20, 2)                          # step array
a8 = np.linspace(0, 1, 6)                         # evenly spaced
a9 = np.empty((2, 3))                             # uninitialized
a10 = np.zeros_like(a2)                           # zeros with same shape

print("1D array          :", a1)
print("2D array:\n", a2)
print("Zeros (3x3):\n", a3)
print("Ones (2x4):\n", a4)
print("Full with 7:\n", a5)
print("Identity (4x4):\n", a6)
print("Arange(0,20,2)    :", a7)
print("Linspace(0,1,6)   :", a8)

# ─────────────────────────────────────────────────────────
# 2. ARRAY ATTRIBUTES
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("2. ARRAY ATTRIBUTES")
print("="*50)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape    :", arr.shape)
print("Size     :", arr.size)
print("Ndim     :", arr.ndim)
print("Dtype    :", arr.dtype)
print("Itemsize :", arr.itemsize, "bytes")
print("Nbytes   :", arr.nbytes, "bytes")

# ─────────────────────────────────────────────────────────
# 3. INDEXING & SLICING
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("3. INDEXING & SLICING")
print("="*50)

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Element [1,2]      :", arr[1, 2])          # 60
print("Row 0              :", arr[0])
print("Col 1              :", arr[:, 1])
print("Sub-array [0:2,1:] :\n", arr[0:2, 1:])
print("Reverse rows       :\n", arr[::-1])

# Boolean indexing
print("Elements > 50      :", arr[arr > 50])

# Fancy indexing
print("Fancy rows [0,2]   :\n", arr[[0, 2]])

# ─────────────────────────────────────────────────────────
# 4. RESHAPING & MANIPULATION
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("4. RESHAPING & MANIPULATION")
print("="*50)

a = np.arange(1, 13)
print("Original           :", a)
print("Reshape (3,4):\n",   a.reshape(3, 4))
print("Reshape (2,2,3):\n", a.reshape(2, 2, 3))
print("Flatten            :", a.reshape(3, 4).flatten())
print("Ravel              :", a.reshape(3, 4).ravel())

b = np.array([[1, 2], [3, 4]])
print("Transpose:\n", b.T)
print("np.transpose:\n", np.transpose(b))

# Stack & split
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("hstack :", np.hstack((x, y)))
print("vstack :\n", np.vstack((x, y)))
print("column_stack:\n", np.column_stack((x, y)))
print("split  :", np.split(np.arange(9), 3))

# ─────────────────────────────────────────────────────────
# 5. ARITHMETIC OPERATIONS
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("5. ARITHMETIC OPERATIONS")
print("="*50)

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Add        :", a + b)
print("Subtract   :", a - b)
print("Multiply   :", a * b)
print("Divide     :", a / b)
print("Floor div  :", a // b)
print("Modulo     :", a % b)
print("Power      :", a ** 2)
print("np.add     :", np.add(a, b))
print("np.multiply:", np.multiply(a, b))
print("np.power   :", np.power(b, 3))

# ─────────────────────────────────────────────────────────
# 6. MATHEMATICAL FUNCTIONS
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("6. MATHEMATICAL FUNCTIONS")
print("="*50)

a = np.array([1.0, 4.0, 9.0, 16.0, 25.0])

print("sqrt       :", np.sqrt(a))
print("cbrt       :", np.cbrt(a))
print("exp        :", np.exp([1, 2, 3]))
print("log        :", np.log(a))
print("log2       :", np.log2(a))
print("log10      :", np.log10(a))
print("abs        :", np.abs([-3, -1, 0, 2]))
print("floor      :", np.floor([1.1, 2.7, -0.5]))
print("ceil       :", np.ceil([1.1, 2.7, -0.5]))
print("round      :", np.round([1.567, 2.345], decimals=1))
print("clip(2,8)  :", np.clip(np.arange(12), 2, 8))

# Trigonometric
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print("\nSin        :", np.round(np.sin(angles), 4))
print("Cos        :", np.round(np.cos(angles), 4))
print("Tan        :", np.round(np.tan(angles), 4))
print("Degrees    :", np.degrees(angles))
print("Radians    :", np.round(np.radians([0, 30, 45, 60, 90]), 4))

# ─────────────────────────────────────────────────────────
# 7. STATISTICAL FUNCTIONS
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("7. STATISTICAL FUNCTIONS")
print("="*50)

data = np.array([[4, 7, 2, 9],
                 [3, 5, 8, 1],
                 [6, 0, 4, 7]])

print("Min            :", np.min(data))
print("Max            :", np.max(data))
print("Sum            :", np.sum(data))
print("Mean           :", np.mean(data))
print("Median         :", np.median(data))
print("Std dev        :", np.round(np.std(data), 4))
print("Variance       :", np.round(np.var(data), 4))

print("\nAxis=0 (col) sum:", np.sum(data, axis=0))
print("Axis=1 (row) sum:", np.sum(data, axis=1))
print("Axis=0 mean    :", np.mean(data, axis=0))
print("Cumsum (flat)  :", np.cumsum(data))
print("Cumprod row0   :", np.cumprod(data[0]))
print("Percentile 25  :", np.percentile(data, 25))
print("Percentile 75  :", np.percentile(data, 75))
print("Argmin         :", np.argmin(data))
print("Argmax         :", np.argmax(data))

# ─────────────────────────────────────────────────────────
# 8. LINEAR ALGEBRA
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("8. LINEAR ALGEBRA")
print("="*50)

A = np.array([[2, 1], [5, 3]])
B = np.array([[1, 0], [2, 1]])

print("Matrix multiply (A@B):\n", A @ B)
print("np.dot(A,B):\n",          np.dot(A, B))
print("Determinant A   :", np.linalg.det(A))
print("Inverse A:\n",             np.linalg.inv(A))
print("Rank A          :", np.linalg.matrix_rank(A))
print("Trace A         :", np.trace(A))

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues     :", eigenvalues)
print("Eigenvectors:\n",          eigenvectors)

# Solve linear system  Ax = b
b_vec = np.array([4, 7])
x = np.linalg.solve(A, b_vec)
print("Solve Ax=b, x   :", x)

# SVD
U, S, Vt = np.linalg.svd(A)
print("SVD - Singular values:", S)

# ─────────────────────────────────────────────────────────
# 9. SORTING & SEARCHING
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("9. SORTING & SEARCHING")
print("="*50)

arr = np.array([5, 1, 9, 3, 7, 2, 8, 4, 6])
print("Original  :", arr)
print("Sorted    :", np.sort(arr))
print("Argsort   :", np.argsort(arr))
print("Where >5  :", np.where(arr > 5))
print("Values >5 :", arr[np.where(arr > 5)])

arr2d = np.array([[3, 1, 4], [2, 5, 0]])
print("Sort axis=1:\n", np.sort(arr2d, axis=1))
print("Unique    :", np.unique([1, 2, 2, 3, 3, 3]))

# ─────────────────────────────────────────────────────────
# 10. SET OPERATIONS
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("10. SET OPERATIONS")
print("="*50)

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 4, 5, 6, 7])

print("Union        :", np.union1d(x, y))
print("Intersection :", np.intersect1d(x, y))
print("Difference   :", np.setdiff1d(x, y))
print("Sym diff     :", np.setxor1d(x, y))
print("isin         :", np.isin([2, 6], x))

# ─────────────────────────────────────────────────────────
# 11. TYPE CONVERSION
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("11. TYPE CONVERSION")
print("="*50)

a = np.array([1.7, 2.3, 3.9])
print("Original float32 :", a.astype(np.float32))
print("To int           :", a.astype(np.int32))
print("To bool          :", a.astype(bool))
print("To complex       :", a.astype(complex))

# ─────────────────────────────────────────────────────────
# 12. NUMPY RANDOM MODULE
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("12. NUMPY RANDOM MODULE")
print("="*50)

rng = npr.default_rng(seed=42)   # reproducible random generator

# Basic random
print("random()         :", npr.random())
print("rand(3,2):\n",        npr.rand(3, 2))
print("randn(3)         :", npr.randn(3))
print("randint(1,10,5)  :", npr.randint(1, 10, 5))

# Distributions
print("\n-- Distributions --")
print("uniform(0,5,4)   :", rng.uniform(0, 5, 4))
print("normal(0,1,4)    :", rng.normal(0, 1, 4))
print("binomial(10,.5,4):", rng.binomial(10, 0.5, 4))
print("poisson(3,5)     :", rng.poisson(3, 5))
print("exponential(1,4) :", rng.exponential(1, 4))
print("beta(2,5,4)      :", rng.beta(2, 5, 4))
print("gamma(2,1,4)     :", rng.gamma(2, 1, 4))
print("chisquare(2,4)   :", rng.chisquare(2, 4))

# Sampling & shuffling
arr = np.arange(10)
print("\nOriginal         :", arr)
npr.shuffle(arr)
print("After shuffle    :", arr)
print("Choice(5, 3, no replace):", npr.choice(np.arange(5), 3, replace=False))
print("Permutation      :", npr.permutation(6))

# ─────────────────────────────────────────────────────────
# 13. BROADCASTING
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("13. BROADCASTING")
print("="*50)

# Rule: dimensions are compared right-to-left;
# they must be equal OR one of them must be 1.

# Case 1: scalar with array
a = np.array([1, 2, 3, 4])
print("Array + 10       :", a + 10)

# Case 2: 1D + 2D
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row    = np.array([10, 20, 30])       # shape (3,)
print("Matrix + row:\n", matrix + row)

# Case 3: column vector + row vector → 2D grid
col = np.array([[1], [2], [3]])       # shape (3,1)
row2 = np.array([10, 20, 30])         # shape (3,)  → treated as (1,3)
print("col + row2 (outer sum):\n", col + row2)

# Case 4: 3D broadcasting
a3d  = np.ones((3, 1, 4))
b2d  = np.ones((1, 5, 1))
result = a3d + b2d
print("3D broadcast shape (3,1,4)+(1,5,1) →", result.shape)

# Practical use: subtract mean from each column
data = np.array([[1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0],
                 [7.0, 8.0, 9.0]])
col_means = data.mean(axis=0)          # shape (3,)
normalized = data - col_means          # broadcast subtraction
print("Col means        :", col_means)
print("Normalized:\n", normalized)

# Euclidean distance matrix via broadcasting
points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=float)
# p[:, np.newaxis] → (4,1,2),  p[np.newaxis] → (1,4,2)
diff   = points[:, np.newaxis] - points[np.newaxis]   # (4,4,2)
dist   = np.sqrt((diff**2).sum(axis=2))
print("Euclidean distance matrix:\n", np.round(dist, 3))

# ─────────────────────────────────────────────────────────
# 14. LOGICAL & COMPARISON OPERATIONS
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("14. LOGICAL & COMPARISON")
print("="*50)

a = np.array([1, 2, 3, 4, 5])
print("a > 3           :", a > 3)
print("a == 3          :", a == 3)
print("a != 3          :", a != 3)
print("(a>1)&(a<5)     :", (a > 1) & (a < 5))
print("(a<2)|(a>4)     :", (a < 2) | (a > 4))
print("np.any(a>4)     :", np.any(a > 4))
print("np.all(a>0)     :", np.all(a > 0))
print("np.logical_not  :", np.logical_not([True, False, True]))
print("np.isnan        :", np.isnan([1, np.nan, 3]))
print("np.isinf        :", np.isinf([1, np.inf, 3]))

# ─────────────────────────────────────────────────────────
# 15. SAVE & LOAD
# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("15. SAVE & LOAD")
print("="*50)

arr = np.array([1, 2, 3, 4, 5])

# Binary .npy
np.save("/tmp/my_array.npy", arr)
loaded = np.load("/tmp/my_array.npy")
print("Saved & loaded (npy) :", loaded)

# Multiple arrays .npz
np.savez("/tmp/multi.npz", a=arr, b=arr * 2)
data_npz = np.load("/tmp/multi.npz")
print("Loaded npz a         :", data_npz['a'])
print("Loaded npz b         :", data_npz['b'])

# CSV text format
np.savetxt("/tmp/arr.csv", arr.reshape(1, -1), delimiter=",", fmt="%d")
loaded_csv = np.loadtxt("/tmp/arr.csv", delimiter=",")
print("Loaded csv           :", loaded_csv)

# ─────────────────────────────────────────────────────────
print("\n" + "="*50)
print("  ALL NUMPY OPERATIONS COMPLETED SUCCESSFULLY!")
print("="*50 + "\n")