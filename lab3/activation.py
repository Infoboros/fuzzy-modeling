from utils import print_table


class Activation:
    def __init__(self, Cs: [[float]], indexes: [int]):
        self.Cs = Cs
        self.indexes = indexes

    def activate(self) -> [float]:
        activate_rows = [
            self.Cs[index]
            for index in self.indexes
        ]
        return list(
            map(
                max,
                list(zip(*activate_rows))
            )
        )

    def __str__(self):
        return f'lB{str(self.__class__).split("lB")[1][0]}'


class lB1(Activation):
    def __init__(self, Cs: [[float]]):
        super().__init__(Cs, [0, 1])


class lB2(Activation):
    def __init__(self, Cs: [[float]]):
        super().__init__(Cs, [2, 3, 4])


class lB3(Activation):
    def __init__(self, Cs: [[float]]):
        super().__init__(Cs, [5, 6, 7, 8, 9])


class lB4(Activation):
    def __init__(self, Cs: [[float]]):
        super().__init__(Cs, [10, 11, 12, 13])


class lB5(Activation):
    def __init__(self, Cs: [[float]]):
        super().__init__(Cs, [14, 15, 16, 17, 18])


class ActivateProcessor:
    def __init__(self, lBs):
        self.lBs = lBs

    def process(self) -> [[float]]:
        results = [lB.activate() for lB in self.lBs]

        print_table(
            list(zip(*results)),
            map(str, self.lBs)
        )

        return results

