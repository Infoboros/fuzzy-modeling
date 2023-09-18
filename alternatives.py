from tabulate import tabulate

from criteria import Criteria, FuzzyCriteria, QualitativeCriteria
from utils import print_indexes_list


class Alternatives:
    def __init__(self, alternatives: [str], quantitative: [[float]], qualitative: [[[float]]]):
        self.alternatives = alternatives
        self.quantitative = quantitative
        self.qualitative = qualitative

    @staticmethod
    def get_symbol(index: int) -> str:
        return chr(ord('A') + index)

    @staticmethod
    def get_name_for_criteries(criteries: [Criteria]) -> [str]:
        return [criteria.name for criteria in criteries]

    def print_criteries(self, criteries_quantitative: [FuzzyCriteria], criteries_qualitative: [QualitativeCriteria]):
        criteria_names = self.get_name_for_criteries(criteries_quantitative + criteries_qualitative)
        print_indexes_list('Критерии', criteria_names)
        print_indexes_list('Альтернативы', self.alternatives)

        print()
        print(f'Оценка для количественных критериев')
        print(tabulate(
            [
                [self.alternatives[index]] + quantitative
                for index, quantitative in enumerate(self.quantitative)
            ],
            headers=[''] + self.get_name_for_criteries(criteries_quantitative)
        ))

        print()
        print('Оценки для качественных критериев')
        for index, criteria in enumerate(criteries_qualitative):
            avg_geometry = criteria.get_avg_geometry(self.qualitative[index])
            eigenvalues = criteria.get_eigenvalues(avg_geometry)
            print()
            print(tabulate(
                [
                    [self.alternatives[index]] + quantitative + [avg_geometry[index]] + [eigenvalues[index]]
                    for index, quantitative in enumerate(self.qualitative[index])
                ],
                headers=[criteria.name] + self.alternatives + ['Cред.геом.', 'Соб.вектор']
            ))

    def print_symbols(self):
        print()
        for index, altenative in enumerate(self.alternatives):
            print(f'{self.get_symbol(index)}) {altenative}')

    def get_sets(self, criteries_quantitative: [FuzzyCriteria]):
        transposed_quantitative = list(zip(*self.quantitative))
        quantitative_sets = []
        for index, criteria in enumerate(criteries_quantitative):
            print()
            print(f'{index + 1}. {criteria.name}')
            criteria.print_criteria()
            criteria_set = criteria.get_set(transposed_quantitative[index])

            print(
                f'K{index + 1} = {"{"}'
                f'{", ".join([f"{alternative_criteria}/{self.get_symbol(index)}" for index, alternative_criteria in enumerate(criteria_set)])}'
                f'{"}"}'
            )

            quantitative_sets.append(criteria_set)

        return quantitative_sets
