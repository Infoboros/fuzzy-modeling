from utils import print_table


class Accumulation:
    def __init__(self, Bs: [[float]], funk):
        self.Bs = Bs
        self.funk = funk

    def accumulate(self) -> [float]:
        return list(
            map(
                self.funk,
                list(zip(*self.Bs))
            )
        )


class AccumulationProcessor:
    def __init__(self, accumulation: Accumulation):
        self.accumulation = accumulation

    def process(self) -> [float]:
        result = self.accumulation.accumulate()

        print_table(
            [[r] for r in result],
            ["B"]
        )

        return result
