from composite_rule import CompositeRule
from implication import ImplicationSet, Implication
from linguistic_variable import LinguisticVariable
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

target_linguistic_variable = LinguisticVariable(
    'степень соответствия с целью',
    ("соответствует", "более чем соответствует", "абсолютно соответствует", "очень соответствует", "не соответствует"),
    (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0),
    [
        {
            'str': 'μT1(x)=x,x∈I',
            'func': lambda x: x
        },
        {
            'str': 'μT2(x)=√(x^3),x∈I',
            'func': lambda x: x ** (3 / 2)
        },
        {
            'str': 'μT3(x)={1,x=1;0,x≠1),x∈I',
            'func': lambda x: 1 if x == 1 else 0
        },
        {
            'str': 'μT4(x)=x^2,x∈I',
            'func': lambda x: x ** 2
        },
        {
            'str': ' μT5(x)=1-x,x∈I',
            'func': lambda x: 1 - x
        }
    ]
)

composite_rules = CompositeRule(
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
    ]],
    target_linguistic_variable
)

implication_rules = ImplicationSet([
    Implication(
        [
            FuzzyCriteria(
                'быстро формирует четверостишия',
                get_normal(9, 2),
                (9, 15),
                0.1
            ),
            FuzzyCriteria(
                'обладает высоким качеством стихотворного текста',
                get_normal(5, 1),
                (0, 5),
                0.1
            ),
        ],
        'удовлетворительный'
    ),
    Implication(
        [
            FuzzyCriteria(
                'быстро формирует четверостишия',
                get_normal(9, 2),
                (9, 15),
                0.1
            ),
            FuzzyCriteria(
                'обладает высоким качеством стихотворного текста',
                get_normal(5, 1),
                (0, 5),
                0.1
            ),
            FuzzyCriteria(
                'быстрым процессом обучения',
                get_normal(2, 1),
                (2, 5),
                0.1
            ),
            FuzzyCriteria(
                'высоким количеством настроечных параметров',
                get_normal(10, 2),
                (0, 10),
                0.1
            ),
        ],
        'более чем удовлетворительный'
    ),
    Implication(
        [
            FuzzyCriteria(
                'быстро формирует четверостишия',
                get_normal(9, 2),
                (9, 15),
                0.1
            ),
            FuzzyCriteria(
                'обладает высоким качеством стихотворного текста',
                get_normal(5, 1),
                (0, 5),
                0.1
            ),
            FuzzyCriteria(
                'быстрым процессом обучения',
                get_normal(2, 1),
                (2, 5),
                0.1
            ),
            FuzzyCriteria(
                'высоким количеством настроечных параметров',
                get_normal(10, 2),
                (0, 10),
                0.1
            ),
            FuzzyCriteria(
                'поддерживает много языков програмирования',
                get_normal(5, 2),
                (0, 5),
                0.1
            ),
            QualitativeCriteria('обладает удобным API')
        ],
        'безупречный'
    ),
    Implication(
        [
            FuzzyCriteria(
                'быстро формирует четверостишия',
                get_normal(9, 2),
                (9, 15),
                0.1
            ),
            FuzzyCriteria(
                'обладает высоким качеством стихотворного текста',
                get_normal(5, 1),
                (0, 5),
                0.1
            ),
            FuzzyCriteria(
                'быстрым процессом обучения',
                get_normal(2, 1),
                (2, 5),
                0.1
            ),
            FuzzyCriteria(
                'высоким количеством настроечных параметров',
                get_normal(10, 2),
                (0, 10),
                0.1
            ),
            QualitativeCriteria('обладает удобным API')
        ],
        'очень удовлетворительный'
    ),
    Implication(
        [
            FuzzyCriteria(
                'быстро формирует четверостишия',
                lambda x: 1 - get_normal(9, 2)(x),
                (9, 15),
                0.1
            ),
            FuzzyCriteria(
                'обладает высоким качеством стихотворного текста',
                lambda x: 1 - get_normal(5, 1)(x),
                (0, 5),
                0.1
            ),
            FuzzyCriteria(
                'быстрым процессом обучения',
                lambda x: 1 - get_normal(2, 1)(x),
                (2, 5),
                0.1
            ),
            FuzzyCriteria(
                'высоким количеством настроечных параметров',
                lambda x: 1 - get_normal(10, 2)(x),
                (0, 10),
                0.1
            ),
        ],
        'неудовлетворительный'
    )
])
alternatives_indexes_for_implications = [
    (0, 3),
    (0, 3, 1, 2),
    (0, 3, 1, 2, 4, -1),
    (0, 3, 1, 2, -1),
    (0, 3, 1, 2),
]

composite_rules.print_criteries(
    criteries_quantitative,
    criteries_qualitative
)

print()
print('Правила вывода')
print(str(implication_rules))

print()
print('Лингвистическая переменная соответствия с целью')
target_linguistic_variable.print()

print()
print('Оценки альтернатив по каждому из критериев')
composite_rules.print_u_for_x(criteries_quantitative, criteries_qualitative)

print()
print('Перевод правил')
Ms = composite_rules.get_m(implication_rules, alternatives_indexes_for_implications)

print()
print('Преобразование полученных импликаций')
Ds = composite_rules.get_d(Ms, range(5))

print()
print('Определим обобщенную цель: D ̃:D ̃=П(i=1;5)D ̃i')
aggregate_Ds = composite_rules.get_aggregate_d(Ds)

print()
print('Произведем точечную оценку')
Fa = composite_rules.get_Fa(aggregate_Ds)

composite_rules.ranging(Fa)
