from criteria import Criteria, A1, B1, A4
from utils import print_table


class PredActivation:
    def __init__(self, Al, left: Criteria, right: Criteria, implication):
        self.Al = Al
        self.left = left
        self.right = right
        self.implication = implication

    def activate(self) -> [float]:
        implication_result = [
            [
                self.implication(self.left.func(x), self.right.func(y))
                for y in self.right.interval
            ]
            for x in self.left.interval
        ]
        transpose_implication_result = list(zip(*implication_result))
        return [
            sum(
                map(
                    lambda pair: pair[0] * pair[1],
                    zip(self.Al, column)
                )
            )
            for column in transpose_implication_result
        ]


class C1(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A1(), B1(), implication)


class C2(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A4(), B1(), implication)


class PreadActivationProcess:
    def __init__(self, Cs: [PredActivation]):
        self.Cs = Cs

    def process(self) -> [[float]]:
        results = [C.activate() for C in self.Cs]
        header = [""] + list(self.Cs[0].right.interval)
        table = [
            [f"C{index + 1}"] + row
            for index, row in enumerate(results)
        ]

        print_table(
            table,
            header
        )

        return results
