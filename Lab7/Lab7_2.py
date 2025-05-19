# Implementation of scaling and PCA algorithms in pure Python

import math
from functools import partial


# Helper functions
def shape(A):
    """Return (num_rows, num_cols) of matrix A."""
    return len(A), len(A[0]) if A else (0, 0)


def get_column(A, j):
    """Return the j-th column of matrix A."""
    return [row[j] for row in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """Create a num_rows x num_cols matrix whose (i,j)-entry is entry_fn(i, j)."""
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def mean(x):
    """Compute the mean of a list of numbers."""
    return sum(x) / len(x)


def sum_of_squares(x):
    """Return sum of squared deviations from mean."""
    m = mean(x)
    return sum((xi - m) ** 2 for xi in x)


def standard_deviation(x):
    """Compute standard deviation of a list of numbers."""
    return math.sqrt(sum_of_squares(x) / (len(x) - 1))


def dot(v, w):
    """Dot product of two vectors."""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def magnitude(v):
    """Return the magnitude (length) of vector v."""
    return math.sqrt(dot(v, v))


def vector_add(v, w):
    """Add two vectors."""
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    """Subtract w from v."""
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def scalar_multiply(c, v):
    """Multiply vector v by scalar c."""
    return [c * v_i for v_i in v]


def vector_sum(vectors):
    """Sum up a list of vectors."""
    result = vectors[0]
    for v in vectors[1:]:
        result = vector_add(result, v)
    return result


# Distance function
def distance(v, w):
    """Euclidean distance between vectors v and w."""
    return magnitude(vector_subtract(v, w))


# Scaling functions
def scale(data_matrix):
    """Return means and standard deviations for each column."""
    num_rows, num_cols = shape(data_matrix)
    means = [mean(get_column(data_matrix, j)) for j in range(num_cols)]
    stdevs = [standard_deviation(get_column(data_matrix, j)) for j in range(num_cols)]
    return means, stdevs


def rescale(data_matrix):
    """Scale data so each column has mean 0 and std deviation 1; skip zero-stdev columns."""
    means, stdevs = scale(data_matrix)
    num_rows, num_cols = shape(data_matrix)

    def rescaled(i, j):
        if stdevs[j] > 0:
            return (data_matrix[i][j] - means[j]) / stdevs[j]
        else:
            return data_matrix[i][j]

    return make_matrix(num_rows, num_cols, rescaled)


# Centering function
def de_mean_matrix(A):
    """Subtract column means from A, so each column has mean zero."""
    num_rows, num_cols = shape(A)
    column_means, _ = scale(A)
    return make_matrix(num_rows, num_cols,
                       lambda i, j: A[i][j] - column_means[j])


# PCA-related functions
def direction(w):
    """Return the unit vector in the direction of w."""
    mag = magnitude(w)
    return [w_i / mag for w_i in w]


def directional_variance_i(x_i, w):
    """Variance of row x_i in direction w."""
    return dot(x_i, direction(w)) ** 2


def directional_variance(X, w):
    """Total variance of data X in direction w."""
    return sum(directional_variance_i(x_i, w) for x_i in X)


def directional_variance_gradient_i(x_i, w):
    """Gradient contribution from x_i to directional variance."""
    projection_length = dot(x_i, direction(w))
    return [2 * projection_length * x_ij for x_ij in x_i]


def directional_variance_gradient(X, w):
    """Gradient of directional variance for data X."""
    return vector_sum([directional_variance_gradient_i(x_i, w) for x_i in X])


# Optimization routines
def maximize_batch(target_fn, gradient_fn, theta_0, step_size=0.01, tolerance=1e-6, max_iter=1000):
    """Batch gradient ascent."""
    theta = theta_0[:]
    for _ in range(max_iter):
        grad = gradient_fn(theta)
        next_theta = vector_add(theta, scalar_multiply(step_size, grad))
        if distance(next_theta, theta) < tolerance:
            break
        theta = next_theta
    return theta


def maximize_stochastic(target_fn_i, gradient_fn_i, X, y, theta_0,
                        step_size=0.01, tolerance=1e-6, max_iter=1000):
    """Stochastic gradient ascent."""
    theta = theta_0[:]
    for _ in range(max_iter):
        change = 0
        for x_i, y_i in zip(X, y):
            grad_i = gradient_fn_i(x_i, y_i, theta)
            update = scalar_multiply(step_size, grad_i)
            theta = vector_add(theta, update)
            change += magnitude(update)
        if change < tolerance:
            break
    return theta


def first_principal_component(X):
    """Return the first principal component (unit vector) of X."""
    guess = [1 for _ in X[0]]
    unscaled_maximizer = maximize_batch(
        partial(directional_variance, X),
        partial(directional_variance_gradient, X),
        guess
    )
    return direction(unscaled_maximizer)


def first_principal_component_sgd(X):
    """Return the first principal component using stochastic gradient ascent."""
    guess = [1 for _ in X[0]]
    unscaled = maximize_stochastic(
        lambda x, _, w: directional_variance_i(x, w),
        lambda x, _, w: directional_variance_gradient_i(x, w),
        X,
        [None for _ in X],
        guess
    )
    return direction(unscaled)


# Projection functions
def project(v, w):
    """Project vector v onto direction w."""
    projection_length = dot(v, w)
    return scalar_multiply(projection_length, w)


def remove_projection_from_vector(v, w):
    """Remove the projection of v on w from v."""
    return vector_subtract(v, project(v, w))


def remove_projection(X, w):
    """Remove projection of each row of X on w."""
    return [remove_projection_from_vector(x_i, w) for x_i in X]


# Transformation functions
def transform_vector(v, components):
    """Transform vector v into PCA space defined by components."""
    return [dot(v, w) for w in components]


def transform(X, components):
    """Transform dataset X into PCA space defined by components."""
    return [transform_vector(x_i, components) for x_i in X]


# Example usage
if __name__ == "__main__":
    data = [
        [63, 150],
        [67, 160],
        [70, 171]
    ]
    # Rescale and compute distances
    rescaled_data = rescale(data)
    print("Rescaled Data:", rescaled_data)

    # PCA
    centered = de_mean_matrix(rescaled_data)
    pc1 = first_principal_component(centered)
    print("First Principal Component:", pc1)

    # Project data on PC1
    projections = [project(row, pc1) for row in centered]
    print("Projections on PC1:", projections)

# End of module
