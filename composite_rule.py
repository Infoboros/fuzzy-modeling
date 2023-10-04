from criteria import FuzzyCriteria, QualitativeCriteria
from implication import ImplicationSet
from linguistic_variable import LinguisticVariable
from many_criteria_choice import ManyCriteriaChoice
from utils import max_norm_vector, print_table


class CompositeRule(ManyCriteriaChoice):
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

    def get_d(self, ms: [[float]], linguistic_variable: LinguisticVariable, Tu_indexes: [int]):
        u_column = [f'u{index + 1}' for index in range(len(ms))]
        i_header = list(map(str, linguistic_variable.I))

        Ds = []
        for index_d, m in enumerate(ms, start=1):
            d = [
                [
                    min(1, 1 - m_el + linguistic_variable.us[Tu_indexes[index_d - 1]]['func'](i))
                    for i in linguistic_variable.I
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

    def get_aggregate_d(self, ds: [[[float]]], linguistic_variable: LinguisticVariable):
        u_column = [f'u{index + 1}' for index in range(len(ds[0]))]
        i_header = list(map(str, linguistic_variable.I))

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