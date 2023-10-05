from composite_rule import CompositeRule
from implication import ImplicationSet, Implication
from linguistic_variable import LinguisticVariable
from criteria import FuzzyCriteria, QualitativeCriteria


def k1(x):
    return {
        1650: 0.75,
        1450: 0.55,
        1199: 0.35,
        2199: 1,
        1399: 0.4
    }[x]


def k2(x):
    return {
        20: 0.8,
        15: 0.7,
        10: 0.6,
        30: 1
    }[x]


def k3(x):
    return {
        300: 1,
        150: 0.55
    }[x]


def k4(x):
    return {
        5: 0.5,
        1: 0.1,
        4: 0.4,
        6: 0.6
    }[x]


def k5(x):
    return {
        204: 0.21,
        170: 0.15,
        220: 0.23,
        680: 0.7,
        200: 0.2
    }[x]


def k6(row_x):
    s = sum(row_x)
    if s >= 14:
        return 0.9
    if s > 8:
        return 0.65
    if s > 3:
        return 0.4
    return 0.3


criteries_quantitative = [
    FuzzyCriteria(
        'Стоимость',
        k1,
        (600, 2400),
        1
    ),
    FuzzyCriteria(
        'Длина распространения сигнала',
        k2,
        (0, 30),
        5
    ),
    FuzzyCriteria(
        'Пропускная способность',
        k3,
        (0, 350),
        50
    ),
    FuzzyCriteria(
        'Количество VLAN портов',
        k4,
        (0, 6),
        1
    ),
    FuzzyCriteria(
        'Вес',
        k5,
        (150, 750),
        50
    ),
]
criteries_qualitative = [QualitativeCriteria('Известность бренда')]

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
        'D-Link DIR-620A',
        'Zyxel Keenetic Start II',
        'D-Link DIR-320A',
        'TP-LINK Archer C50',
        'NetGear WNR614-100',
    ],
    [
        [1650, 20, 300, 5, 204],
        [1450, 15, 300, 1, 170],
        [1199, 10, 150, 4, 220],
        [2199, 30, 300, 6, 680],
        [1399, 15, 300, 4, 200],
    ],
    [[
        [1, 4, 1, 3, 5],
        [0.25, 1, 0.25, 0.3333, 2],
        [1, 4, 1, 3, 5],
        [0.33333, 3, 0.33333, 1, 4],
        [0.2, 0.5, 0.2, 0.25, 1]
    ]],
    target_linguistic_variable
)

implication_rules = ImplicationSet([
    Implication(
        [
            FuzzyCriteria(
                'не дорогой',
                lambda x: 1 - k1(x),
                (600, 2400),
                1
            ),
            FuzzyCriteria(
                'обладает высокой пропускной способностью',
                k3,
                (0, 350),
                50
            ),
        ],
        'удовлетворительный'
    ),
    Implication(
        [
            FuzzyCriteria(
                'обладает большим сигналом распространения',
                k2,
                (0, 30),
                5
            ),
            FuzzyCriteria(
                'большим количеством VLAN портов',
                k4,
                (0, 6),
                1
            ),
        ],
        'более чем удовлетворительный'
    ),
    Implication(
        [
            FuzzyCriteria(
                'обладает большим сигналом распространения',
                k2,
                (0, 30),
                5
            ),
            FuzzyCriteria(
                'большим количеством VLAN портов',
                k4,
                (0, 6),
                1
            ),
            FuzzyCriteria(
                'обладает малым весом',
                lambda x: 1 - k5(x),
                (150, 750),
                50
            ),
            FuzzyCriteria(
                'является товаром известного бренда',
                k6,
                (150, 750),
                50
            ),
        ],
        'безупречный'
    ),
    Implication(
        [
            FuzzyCriteria(
                'не дорогой',
                lambda x: 1 - k1(x),
                (600, 2400),
                1
            ),
            FuzzyCriteria(
                'с высокой пропускной способностью',
                k3,
                (0, 350),
                50
            ),
            FuzzyCriteria(
                'с большим сигналом распространения',
                k2,
                (0, 30),
                5
            ),
        ],
        'очень удовлетворительный'
    ),
    Implication(
        [
            FuzzyCriteria(
                'дорогой',
                k1,
                (600, 2400),
                1
            ),
            FuzzyCriteria(
                'с низкой пропускной способностью',
                lambda x: 1 - k3(x),
                (0, 350),
                50
            ),
            FuzzyCriteria(
                'с малым сигналом распространения',
                lambda x: 1 - k2(x),
                (0, 30),
                5
            ),
        ],
        'неудовлетворительный'
    )
])
alternatives_indexes_for_implications = [
    (0, 2),
    (1, 3),
    (1, 3, 4, -1),
    (0, 2, 1),
    (0, 2, 1),
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
