from criteria import Criteria, FuzzyCriteria, QualitativeCriteria
from utils import print_indexes_list, print_table, max_norm_vector
from math import log, sqrt


class ManyCriteriaChoice:
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

        print_table(
            [
                [self.alternatives[index]] + quantitative
                for index, quantitative in enumerate(self.quantitative)
            ],
            [''] + self.get_name_for_criteries(criteries_quantitative),
            'Оценка для количественных критериев'
        )

        print()
        print('Оценки для качественных критериев')
        for index, criteria in enumerate(criteries_qualitative):
            avg_geometry = criteria.get_avg_geometry(self.qualitative[index])
            eigenvalues = criteria.get_eigenvalues(avg_geometry)

            print_table(
                [
                    [self.alternatives[index]] + quantitative + [avg_geometry[index]] + [eigenvalues[index]]
                    for index, quantitative in enumerate(self.qualitative[index])
                ],
                [criteria.name] + self.alternatives + ['Cред.геом.', 'Соб.вектор']
            )

    def print_symbols(self):
        print()
        for index, altenative in enumerate(self.alternatives):
            print(f'{self.get_symbol(index)}) {altenative}')

    def get_sets(self, criteries_quantitative: [FuzzyCriteria], criteries_qualitative: [QualitativeCriteria]):
        transposed_quantitative = list(zip(*self.quantitative))
        quantitative_sets = []
        for index, criteria in enumerate(criteries_quantitative):
            print()
            print(f'{index + 1}. {criteria.name}')
            # criteria.print_criteria()
            criteria_set = criteria.get_set(transposed_quantitative[index])

            print(
                f'K{index + 1} = {"{"}'
                f'{", ".join([f"{alternative_criteria}/{self.get_symbol(index)}" for index, alternative_criteria in enumerate(criteria_set)])}'
                f'{"}"}'
            )

            quantitative_sets.append(criteria_set)

        qualitative_sets = []
        for index, qualitative in enumerate(self.qualitative):
            criteria = criteries_qualitative[index]
            qualitative_sets.append(
                criteria.get_eigenvalues(
                    criteria.get_avg_geometry(
                        qualitative
                    )
                )
            )

        return quantitative_sets + qualitative_sets

    def get_generalized_criteria(self, sets):
        header = [''] + [f'K{index}' for index, fuzzy_set in enumerate(sets, start=1)] + ['MIN']
        normalized_sets = [
            max_norm_vector(vector)
            for vector in sets
        ]
        transposed_normalized_sets = list(zip(*normalized_sets))
        minimums = [min(vector) for vector in transposed_normalized_sets]

        print_table(
            [
                [self.get_symbol(index)] + list(row) + [minimums[index]]
                for index, row in enumerate(transposed_normalized_sets)
            ]
            +
            [['MAX'] + ([''] * len(transposed_normalized_sets[0])) + [max(minimums)]],
            header
        )

        return minimums

    @staticmethod
    def de_fuzzy(vector):
        return [
            1 if el > 0.5 else 0
            for el in vector
        ]

    @staticmethod
    def hemming(vector):
        return [
            1 - el if el > 0.5 else el
            for el in vector
        ]

    @staticmethod
    def evklid(vector):
        return [
            el ** 2
            for el in ManyCriteriaChoice.hemming(vector)
        ]

    @staticmethod
    def normalize(vector):
        summary = sum(vector)
        return [
            el / summary
            for el in vector
        ]

    @staticmethod
    def entropy(vector):
        return [
            el * log(el)
            for el in vector
        ]

    def print_distance(self, generalized_criteria):
        de_fuzzy = self.de_fuzzy(generalized_criteria)

        hemming = self.hemming(generalized_criteria)
        sum_hemming = sum(hemming)
        norm_hemming = sum_hemming / len(generalized_criteria)
        hemming_distance = norm_hemming * 2

        evklid = self.evklid(generalized_criteria)
        sum_evklid = sum(evklid)
        sqrt_evklid = sqrt(sum_evklid)
        norm_evklid = sqrt_evklid / sqrt(len(generalized_criteria))
        evklid_distance = norm_evklid * 2

        normalize = self.normalize(evklid)
        entropy = self.entropy(normalize)
        sum_entropy = sum(entropy)
        entropy_distance = - 1 / log(len(generalized_criteria)) * sum_entropy

        table = [
            generalized_criteria + ['Сумма', '', '', ''],
            de_fuzzy + [sum(de_fuzzy), '', 'Нормированные', 'ИН'],
            hemming + [sum_hemming, 'sqrt', norm_hemming, hemming_distance],
            evklid + [sum_evklid, sqrt_evklid, norm_evklid, evklid_distance],
            normalize + [sum(normalize), '', '', 'enthropy'],
            entropy + [sum_entropy, '', '', entropy_distance]
        ]

        print_table(
            list(zip(*table)),
            ['Ki', 'Четкое', 'Хемминг', 'Евклид', 'Нормировка', 'Энтропия'],
            'Оценка индекса нечеткости'
        )
