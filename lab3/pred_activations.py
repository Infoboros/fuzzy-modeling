from criteria import Criteria, A1, B1, A4, B2, A2, A3, B3, A5, B4, Al1, B5, Al4, Al2, Al3, Al5
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


class C3(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A1(), B2(), implication)


class C4(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A2(), B2(), implication)


class C5(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A3(), B2(), implication)


class C6(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A1(), B3(), implication)


class C7(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A4(), B3(), implication)


class C8(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A2(), B3(), implication)


class C9(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A3(), B3(), implication)


class C10(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A5(), B3(), implication)


class C11(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A1(), B4(), implication)


class C12(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A4(), B4(), implication)


class C13(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A2(), B4(), implication)


class C14(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A3(), B4(), implication)


class C15(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, Al1(), B5(), implication)


class C16(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, Al4(), B5(), implication)


class C17(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, Al2(), B5(), implication)


class C18(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, Al3(), B5(), implication)


class C19(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, Al5(), B5(), implication)


class C2(PredActivation):
    def __init__(self, Al, implication):
        super().__init__(Al, A4(), B1(), implication)


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
