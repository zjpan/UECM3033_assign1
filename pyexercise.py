import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.cos(x) * sy.exp(-x**2), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array([
    [3,1,3,5,6,3,8,1,9,1],
    [1,2,5,7,1,5,7,1,6,3],
    [6,7,2,1,5,7,9,1,8,9],
    [8,5,7,9,5,3,5,7,9,1],
    [1,5,7,9,3,7,9,2,5,6],
    [7,8,4,2,1,5,7,9,4,1],
    [9,5,4,1,3,5,7,8,1,2],
    [5,7,8,9,5,3,1,5,6,7],
    [1,5,7,9,3,4,5,6,1,6],
    [5,6,7,8,9,6,5,4,5,6]
    ] )
    b = np.array([5,6,8,2,5,6,8,3,1,3])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1308201
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
