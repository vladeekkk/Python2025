import numpy as np

class ArithmeticMixin:
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Different dimensions of matrices for addition")
        return Matrix(self.data + other.data)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Different dimensions of matrices for subtraction")
        return Matrix(self.data - other.data)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Different dimensions of matrices for component-wise multiplication")
        return Matrix(self.data * other.data)

    def __truediv__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Different dimensions of matrices for element-wise division")
        return Matrix(self.data / other.data)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Bad dimensions for matrix multiplication")
        return Matrix(np.matmul(self.data, other.data))


class FileMixin:
    def save_to_file(self, filename):
        np.save(filename, self.data)

    @staticmethod
    def load_from_file(filename):
        data = np.load(filename)
        return Matrix(data)


class StrMixin:
    def __str__(self):
        return np.array2string(self.data, separator=', ') # TODO


class GetterSetterMixin:
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = np.array(data)
        self.rows, self.cols = self.data.shape

class Matrix(ArithmeticMixin, FileMixin, StrMixin, GetterSetterMixin):
    def __init__(self, data):
        self.set_data(data)
