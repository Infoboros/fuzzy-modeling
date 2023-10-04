from criteria import Criteria


class Implication:
    def __init__(self, criteries: [Criteria], consecvent: str):
        self.criteries = criteries
        self.consecvent = consecvent

    def __str__(self):
        return f'Если {" и ".join([criteria.name for criteria in self.criteries])}, то {self.consecvent}'

    def get_m(self, alternatives: [[float]]):
        return list(map(
            min,
            list(zip(*[
                criteria.get_set(alternatives[index])
                for index, criteria in enumerate(self.criteries)
            ]))
        ))


class ImplicationSet:
    def __init__(self, implications: [Implication]):
        self.implications = implications

    def __str__(self):
        return '\n'.join([
            f'{index}. {implication}'
            for index, implication in enumerate(self.implications, start=1)
        ])
