#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_length = len(matrix[0])
    if row_length > 0:
        for row in matrix:
            for i in range(row_length):
                if i == row_length - 1:
                    print("{:d}".format(row[i]))
                else:
                    print("{:d}".format(row[i]), end=" ")
    else:
        print()
