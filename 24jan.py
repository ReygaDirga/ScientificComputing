#GAUSS SEIDEL

import numpy as np
# Define Array
x_arr = [
    [
        [4, -1, 2],
        [3, 6, -1],
        [2, 1, 5],
    ],
    [
        [6, -1, 2, 0],
        [3, 9, 1, -4],
        [1, 2, 7, -1],
        [2, -3, 1, 8],
    ],
    [
        [6, -1, 2, 0, 0],
        [1, 10, 3, -2, 0],
        [2, -1, 12, 1, -4],
        [0, 3, -2, 9, 1],
        [1, -2, 1, 3, 8],
    ]
]

y_arr = [
    [8, 9, 3],
    [12, 18, 14, 4],
    [14, 20, 22, 12, 15],
]

def check_diagonal_dominant(x):
    #change into array
    x = np.array(x)
    #take out the diagonal from the array
    diag = np.diag(np.abs(x))
    #Take out the non-diagonal
    non_diag = np.sum(np.abs(x), axis = 1)
    #Check if the diag >= non_diag
    if np.all(diag >= non_diag - diag):
        return True
    else:
        return False
    
def gauss_seidel(x_array, y_array, max_iteration, epsilon):
    #Change into array
    x = np.array(x_array)
    y = np.array(y_array)
    iteration = max_iteration
    epsilon = epsilon
    diag = np.diag(x)
    
    x = -x
    np.fill_diagonal(x, 0)
    x_old = np.zeros(len(x))
    
    for i in range(iteration):
        x_new = np.array(x_old)
        
        for j, row in enumerate(x):
            #formula gauss-seidel
            x_new[j] = ( y[j] + np.dot(row, x_new)) / diag[j]
            
        print(f"Iteration: {i+1}, {x_new}")
            
        #euclidean_distance 
        euclidean_distance = np.sqrt(np.dot(x_old - x_new, x_old - x_new))
        
        if euclidean_distance < epsilon:
            print(f"Convergence reached at {i+1} iteration")
            print(x_new)
            return True
        
        x_old = x_new
    return False

def run_gauss_seidel(x_arr, y_arr, max_iter, epsilon):
    for i, x in enumerate(x_arr):
        if check_diagonal_dominant(x):
            print("Diagonally Dominant!")
            if gauss_seidel(x, y_arr[i], max_iter, epsilon):
                print("Convergent reached!")
            else:
                print("Not Convergent!")
        else:
            print("Not diagonally dominant!")

run_gauss_seidel(x_arr, y_arr, 20, 0.001)