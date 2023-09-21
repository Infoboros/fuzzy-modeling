from many_criteria_choice import ManyCriteriaChoice
from criteria import FuzzyCriteria, QualitativeCriteria
from utils import get_normal

criteries_quantitative = [
    FuzzyCriteria(
        'Небольшое время формирования четверостишия',
        get_normal(9, 2),
        (9, 15),
        0.1
    ),
    FuzzyCriteria(
        'Быстрый процесс обучения.',
        get_normal(2, 1),
        (2, 5),
        0.1
    ),
    FuzzyCriteria(
        'Большое количество настроечных параметров.',
        get_normal(10, 2),
        (0, 10),
        0.1
    ),
    FuzzyCriteria(
        'Высокое качество стихотворного текста.',
        get_normal(5, 1),
        (0, 5),
        0.1
    ),
    FuzzyCriteria(
        'Поддержка большинства языков программирования.',
        get_normal(5, 2),
        (0, 5),
        0.1
    ),
]
criteries_qualitative = [QualitativeCriteria('Удобство API.')]

criteries = criteries_quantitative + criteries_qualitative

many_criteria_choice = ManyCriteriaChoice(
    [
        'RNNLM',
        'Word2Vec',
        'GloVe',
        'fastText',
        'n-gramm',
    ],
    [
        [10, 3, 7, 3, 2],
        [12, 2.5, 6, 4, 3],
        [9, 2.5, 8, 5, 5],
        [11, 2, 9, 4, 2],
        [10, 3, 7, 3, 1],
    ],
    [[
        [1, 1 / 4, 1, 1 / 3, 5],
        [4, 1, 1 / 4, 1 / 3, 2],
        [1, 4, 1, 3, 5],
        [3, 3, 1 / 3, 1, 4],
        [1 / 5, 1 / 2, 1 / 5, 1 / 4, 1],
    ]]
)

criteria_pairs = [
    [1, 4, 1 / 3, 1 / 3, 3, 5],
    [1 / 4, 1, 1 / 2, 1 / 2, 3, 5],
    [3, 2, 1, 1, 5, 4],
    [3, 2, 1, 1, 5, 5],
    [3, 1 / 3, 1 / 5, 1 / 5, 1, 5],
    [1 / 5, 1 / 5, 1 / 4, 1 / 5, 1 / 5, 1],
]

many_criteria_choice.print_criteries(
    criteries_quantitative,
    criteries_qualitative
)

many_criteria_choice.print_symbols()
sets = many_criteria_choice.get_sets(criteries_quantitative, criteries_qualitative)

print()
print('Определение обобщенного критерия')
generalized_criteria = many_criteria_choice.get_generalized_criteria(sets)
many_criteria_choice.print_distance(generalized_criteria)

alfa = many_criteria_choice.get_alfa(criteries, criteria_pairs)

alfa_sets = many_criteria_choice.sets_to_alfa(sets, alfa)

print()
print('Нормированная матрица критериев с учётом их важности: (возведение в степень alfa)')
alfa_generalized_criteria = many_criteria_choice.get_generalized_criteria(alfa_sets)
many_criteria_choice.print_distance(alfa_generalized_criteria)
many_criteria_choice.print_general_table(alfa_generalized_criteria)
