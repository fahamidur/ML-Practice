## Essential Linear Algebra Topics for ML Engineers

### 1. Fundamental Vector & Matrix Operations

* **Vector Norms:** $L_1$ (Manhattan), $L_2$ (Euclidean), and $L_\infty$ (Maximum).
* **Broadcasting Rules:** How different array shapes interact.
* **Matrix Transposition & Symmetry.**
* **Trace of a Matrix.**
* **Hadamard Product:** Element-wise multiplication.

### 2. Matrix Geometry & Transformations

* **Linear Independence & Basis:** Determining if vectors are redundant.
* **Matrix Rank:** Identifying the dimensionality of the "span."
* **Orthogonal & Orthonormal Matrices:** Matrices where $Q^T Q = I$.
* **Projections:** Projecting a vector onto a subspace (crucial for least squares).
* **Linear Transformations:** Seeing matrices as functions that rotate, scale, or shear space.

### 3. Solving Linear Systems

* **Gaussian Elimination:** The manual "from scratch" method.
* **Matrix Inversion:** Understanding its limitations and computational cost.
* **Pseudo-inverse (Moore-Penrose):** Solving systems that have no exact solution.
* **LU Decomposition:** Factoring a matrix into Lower and Upper triangles.

### 4. Dimensionality Reduction & Decomposition

* **Principal Component Analysis (PCA):** Reducing features while keeping variance.
* **Singular Value Decomposition (SVD):** The "Swiss Army Knife" of linear algebra.
* **Eigen Decomposition:** Finding characteristic vectors ($\mathbf{Av} = \lambda \mathbf{v}$).
* **Non-negative Matrix Factorization (NMF):** Used for topic modeling.

### 5. Advanced Optimization Math

* **Quadratic Forms:** Expressions like $\mathbf{x}^T \mathbf{Ax}$.
* **Positive Semi-Definite (PSD) Matrices:** Checking if a matrix is "valid" for kernels or covariance.
* **The Hessian Matrix:** A matrix of second-order partial derivatives.
* **The Jacobian Matrix:** A matrix of all first-order partial derivatives for vector-valued functions.

### 6. Computational & Specialized Topics

* **Sparse Matrix Representations:** CSR, CSC, and COO formats for high-dimensional, empty data.
* **Tensors:** Multi-dimensional arrays (Generalizing 2D matrices to $N$-dimensions).
* **Numerical Stability:** Understanding underflow/overflow and conditioning.
* **Cholesky Decomposition:** For efficient sampling and solving optimization problems.
