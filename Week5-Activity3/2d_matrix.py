
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions for multiplication: "
                             f"{self.rows}x{self.cols} cannot be multiplied with {other.rows}x{other.cols}")

        # Initialize the result matrix with zeros
        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]

        # Perform matrix multiplication
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]

        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

if __name__ == "__main__":
    # Example usage
    matrix_a = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix_b = Matrix([[7, 8], [9, 10], [11, 12]])

    print("Matrix A:")
    print(matrix_a)
    
    print("\nMatrix B:")
    print(matrix_b)

    result_matrix = matrix_a.multiply(matrix_b)
    print("\nResult of A * B:")
    print(result_matrix)