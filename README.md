# det(ective)🔍: Determinant Detective - Matrix Determinant Calculator

## Introduction 📖

Welcome to the Determinant Detective, a Python program designed to calculate the determinant of a square matrix efficiently. This program ensures user-friendly input validation and error handling to make the process as smooth as possible.

## Table of Contents 📋

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example](#example)
- [Algorithm](#algorithm)
- [Contributing](#contributing)

## Features ✔️

- Calculates the determinant of any square matrix.
- Handles invalid inputs gracefully.
- Works with matrices of various sizes.
- Utilizes a recursive algorithm for determinant calculation.

## Getting Started 🚀

Before you start using the Determinant Detective, make sure you have the following prerequisites installed on your system:

- Python
- NumPy library\*\*

You can install NumPy using pip:

```bash
'pip install numpy'
```

or Anaconda

```Anacondo Prompt
    # Best practice, use an environment rather than install in the base env
    conda create -n my-env
    conda activate my-env
    # If you want to install from conda-forge
    conda config --env --add channels conda-forge
    # The actual install command
    conda install numpy
```

After you installed, activate your own environment and installed numpy via conda, go VSCode and press CTRL + Shift + P. Type:

```VSCode File Researcher
> Python: Select Interpreter
```

Then choose your own environment.
Now you can import and use NumPy.

## Usage 🖥️

To use the Determinant Detective, follow these steps:

1. Run the program in your Python environment (e.g., VSCode).

2. You will be greeted with a welcome message and an introduction to the program.

3. Enter the number of rows and columns for your matrix when prompted. Ensure the following conditions are met:

   - The matrix must have at least one row and one column.
   - Row and column sizes should be positive integers.
   - The matrix should be square (i.e., rows equal columns).

4. Enter the values for each element of the matrix as prompted.

5. The program will calculate and display the determinant of the matrix.

## Example 📝

Lets walk through an example of using the Determinant Detective to calculate the determinant of a 3x3 matrix:

```bash
1 2 3
4 5 6
7 8 9
```

1. Run the program and enter `3` for the number of rows and `3` for the number of columns.

2. Enter the values for each element as prompted.

3. The program will display the determinant, which should be `0` for this particular matrix.

## Algorithm 🧮

The Determinant Detective uses a recursive algorithm for determinant calculation. Here's how it works:

- For 2x2 matrices, it directly calculates the determinant using the formula:

```bash
determinant = (a * d) - (b * c)
```

- For larger matrices, it breaks down the problem into smaller submatrices. It calculates the determinant recursively by calculating the cofactors and submatrices.

## Contributing 🤝

If you'd like to contribute to the Determinant Detective, feel free to fork this repository, make improvements, and create a pull request. We welcome enhancements, bug fixes, and additional features.
