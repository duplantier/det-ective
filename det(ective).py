import numpy as np

# Welcome Messages
print('Welcome to the det(ective): Determinant Detective.')
print('Determinant Detective is able to calculate the determinant of any matrix of any size you will give.')

starter= True
while (starter):
    try: 
        # Take the size of the matrix in terms of rows and columns
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns:"))
        
        # Check if the matrix is zero matrix (0x0)
        if((rows == 0) and (columns == 0)):
            print('A matrix must have at least one row and one column. Please enter valid dimensions.\n')
        # Check if any of the size inputs is negative value.
        elif((rows < 0) or (columns < 0)):
            print('Please enter postive integer values of row and column size of the matrix.\n')
        # Check if the given matrix size DOES NOT represent a square matrix.
        elif (rows != columns):
            print('UNDEFINED.')
            print('Please enter a square matrix size, such as 3x3 or 5x5.\n')
        # If everything is ok:
        else:
            break
    # If any of the inputs is invalid (non-numeric)
    except ValueError:
        print("Invalid input. Please enter a valid numerical value.")
            
    
# Initialize an empty matrix filled with zeros
matrix = np.zeros((rows, columns))
print('')

# Fill the matrix with user inputs
for i in range(rows):
    for j in range(columns):
        while True:  
            # Keep prompting until valid input for all the entries is provided
            try:
                entry = float(input(f"Enter the value for entry at row {i + 1}, column {j + 1}: "))
                matrix[i, j] = entry
                break 
            # If any of the inputs is invalid (non-numeric)
            except ValueError:
                print("Invalid input. Please enter a valid numerical value.")

# Print the given for information
print("\nYour Matrix:")
print(matrix)



def calculateDeterminant(matrix):
    # Get the number of rows and columns of the matrix from the user input
    rows, columns = matrix.shape
    
    # Base case: If the matrix is 2x2, return the determinant
    if rows == 2:
        return (matrix[0, 0] * matrix[1, 1]) - (matrix[0, 1] * matrix[1, 0])
    
    # Initialize the determinant:
    determinant = 0
    
    # 
    for j in range(columns):
        # Calculate the cofactor for the current column
        cofactor = ((-1) ** j) * (matrix[0, j])

        # Recursive logic for calculating the determinant of the submatrix (remained)
        submatrix = np.delete(np.delete(matrix, 0, axis=0), j, axis=1)
        submatrix_determinant = calculateDeterminant(submatrix)

        # Add the contribution of the current column to the determinant
        determinant += (cofactor * submatrix_determinant)

    return determinant


calculated = calculateDeterminant(matrix)


print('\nDeterminant of this matrix is: ' + str(calculated))
