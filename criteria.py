import operator
from abc import ABC, abstractmethod
from functools import reduce

from matplotlib import pyplot as plt


class Criteria(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def print_criteria(self):
        raise NotImplemented()


class FuzzyCriteria(Criteria):

    def __init__(self, name: str, func, range: [float, float], step: float):
        super().__init__(name)
        self.func = func
        self.start, self.stop = range
        self.step = step

    def print_criteria(self):
        ys = []
        current = self.start
        while current <= self.stop:
            ys.append(current)
            current += self.step
        xs = list(map(self.func, ys))
        plt.plot(xs, ys)
        plt.title(self.name)
        plt.show()


class QualitativeCriteria(Criteria):

    def __init__(self, name: str):
        super().__init__(name)

    @staticmethod
    def get_avg_geometry(matrix_pair: [[float]]):
        return [
            pow(reduce(operator.mul, row, 1), 1. / len(matrix_pair))
            for row in matrix_pair
        ]

    @staticmethod
    def get_eigenvalues(avg_geometry: [float]) -> [float]:
        sum_avg_geometry = sum(avg_geometry)
        return list(map(
            lambda geometry: geometry / sum_avg_geometry if sum_avg_geometry else 0.0,
            avg_geometry
        ))

    def print_criteria(self):
        print(f'Качественный критерий')
