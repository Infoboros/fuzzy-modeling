from matplotlib import pyplot as plt

from criteria import FuzzyCriteria, QualitativeCriteria
from implication import ImplicationSet
from linguistic_variable import LinguisticVariable
from many_criteria_choice import ManyCriteriaChoice
from utils import max_norm_vector, print_table


class CompositeRule(ManyCriteriaChoice):
    def __init__(self, alternatives: [str], quantitative: [[float]], qualitative: [[[float]]],
                 linguistic_variable: LinguisticVariable):
        self.linguistic_variable = linguistic_variable
        super().__init__(alternatives, quantitative, qualitative)

    def print_u_for_x(self, criteries_quantitative: [FuzzyCriteria], criteries_qualitative: [QualitativeCriteria]):
        tranposed_quantitative = list(zip(*self.quantitative))
        for index, criteria in enumerate(criteries_quantitative):
            print(f''
                  f'X{index + 1} = '
                  f'"{criteria.name}" = '
                  f'{"{" + ", ".join([f"{u}/u{index}" for index, u in enumerate(criteria.get_set(tranposed_quantitative[index]), start=1)]) + "}"}')

        for index, criteria in enumerate(criteries_qualitative):
            print(f''
                  f'X{index + 1 + len(criteries_quantitative)} = '
                  f'"{criteria.name}" = '
                  f'{"{" + ", ".join([f"{u}/u{index}" for index, u in enumerate(criteria.get_norm_us(self.qualitative[index]), start=1)]) + "}"}')

    def get_m(self, implications: ImplicationSet, alternatives_indexes: [[int]]):
        tranposed_quantitative = list(zip(*self.quantitative))
        ms = []
        for implication_index, implication in enumerate(implications.implications):
            m = implication.get_m([
                tranposed_quantitative[alternative_index] if alternative_index >= 0 else self.qualitative[
                    alternative_index]
                for alternative_index in alternatives_indexes[implication_index]
            ])
            print(
                f'M{implication_index + 1} = {"{" + ", ".join([f"{u}/u{index_u}" for index_u, u in enumerate(m, start=1)]) + "}"}'
            )
            ms.append(m)
        return ms

    def get_d(self, ms: [[float]], Tu_indexes: [int]):
        u_column = [f'u{index + 1}' for index in range(len(ms))]
        i_header = list(map(str, self.linguistic_variable.I))

        Ds = []
        for index_d, m in enumerate(ms, start=1):
            d = [
                [
                    min(1, 1 - m_el + self.linguistic_variable.us[Tu_indexes[index_d - 1]]['func'](i))
                    for i in self.linguistic_variable.I
                ]
                for m_el in m
            ]
            Ds.append(d)
            print_table(
                list(zip(*([u_column] + list(zip(*d))))),
                header=[f'D{index_d}'] + i_header
            )
            print()
        return Ds

    def get_aggregate_d(self, ds: [[[float]]]):
        u_column = [f'u{index + 1}' for index in range(len(ds[0]))]
        i_header = list(map(str, self.linguistic_variable.I))

        aggreagte_d = [
            [
                min([d[row_index][column_index] for d in ds])
                for column_index in range(len(ds[0][0]))
            ]
            for row_index in range(len(ds[0]))
        ]
        print_table(
            list(zip(*([u_column] + list(zip(*aggreagte_d))))),
            header=[f'D~'] + i_header
        )

        return aggreagte_d

    @staticmethod
    def get_intervals_from_A(A):
        zeroed_A = [0] + A
        return [
            (first, second)
            for index in range(len(zeroed_A) - 1)
            if (first := zeroed_A[index]) != (second := zeroed_A[index + 1])
        ]

    def get_Fa_for_alternative(self, A, index):
        print(
            f'A{index}'
            f'={"{" + ", ".join([f"{A[index_i]}/{i}" for index_i, i in enumerate(self.linguistic_variable.I)]) + "}"}'
        )
        print('Уровневые множества')

        integrals = []
        intervals = self.get_intervals_from_A(A)
        for (left, right) in intervals:
            print()
            filtered_I = [
                i
                for index_i, i in enumerate(self.linguistic_variable.I)
                if right <= A[index_i]
            ]
            print(f'A{index}a = {"{" + f"; ".join(map(str, filtered_I)) + "}"} {left} < a <= {right}')
            MA = sum(filtered_I) / len(filtered_I)
            print(f'M(A{index}a)={sum(filtered_I)}/{len(filtered_I)}={MA}')
            integrals.append((left, right, MA))

        Fa = 1 / max(A) * sum([MA * (right - left) for left, right, MA in integrals])
        print()
        print('Точечная оценка')
        print(
            f'F(A{index}) = 1 / {max(A)} ({" + ".join([f"|({round(left, 2)} -> {round(right, 2)}){round(Ma, 4)}da" for left, right, Ma in integrals])})'
        )
        print(
            f'= {1 / max(A)} * ({" + ".join([f"({round(MA * right, 4)} - {round(MA * left, 4)})" for left, right, MA in integrals])})')
        print(f'= {Fa}')

        plt.plot(self.linguistic_variable.I, A)
        plt.scatter(self.linguistic_variable.I, A)
        plt.title(f'u{index}')
        plt.show()
        return Fa

    def get_Fa(self, aggregated_D: [[float]]):
        result = []
        for index, alternative in enumerate(self.alternatives):
            print()
            print(f'{alternative}:')
            result.append(
                self.get_Fa_for_alternative(aggregated_D[index], index + 1)
            )

        return result

    def ranging(self, Fa):
        header = [""] + list(range(1, len(Fa) + 1))
        sorted_fa = sorted(Fa, reverse=True)
        table = [
            ["Название альтернативы"] + self.alternatives,
            ["F(A)"] + Fa,
            ['Ранжирование'] + [str(sorted_fa.index(f) + 1) for f in Fa]
        ]
        print_table(
            table,
            header,
            'Ранжирование альтернатив'
        )

        for index, f in enumerate(sorted_fa, start=1):
            print(f'{index}. {self.alternatives[Fa.index(f)]}')

