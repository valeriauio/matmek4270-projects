import numpy as np


def mesh_function(f, t):
    l = len(t)
    u = np.zeros(l)
    for n in range(0,l):
        u[n] = f(t[n])
    return u    

def func(t):
    if (0 <= t <= 3):
        f = np.exp(-t)
    if (3 < t <= 4):
        f = np.exp(-3*t)
    return f    

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)
