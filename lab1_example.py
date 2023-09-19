from many_criteria_choice import ManyCriteriaChoice
from criteria import FuzzyCriteria, QualitativeCriteria
from utils import get_normal


def k2(x):
    return {
        0: 0,
        5: 0.05,
        10: 0.222,
        15: 0.5,
        20: 0.778,
        25: 0.986,
        30: 1
    }[x]


def k3(x):
    return {
        0: 0,
        50: 0.05,
        100: 0.22,
        150: 0.5,
        200: 0.77777778,
        250: 0.986,
        300: 1,
        350: 1,
    }[x]


def k4(x):
    return {
        0: 0,
        1: 0.056,
        2: 0.22,
        3: 0.5,
        4: 0.778,
        5: 0.944,
        6: 1,
    }[x]

def k5(x):
    return {
        150: 1,
        170: 1,
        200: 0.988,
        204: 0.986,
        220: 0.975,
        250: 0.94444,
        300: 0.875,
        350: 0.77777778,
        400: 0.6527777,
        450: 0.5,
        500: 0.347222,
        550: 0.2222,
        600: 0.1,
        650: 0.05,
        680: 0.027,
        700: 0.01,
        750: 0.01
    }[x]


criteries_quantitative = [
    FuzzyCriteria(
        'Стоимость',
        get_normal(1500, 300),
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

many_criteria_choice = ManyCriteriaChoice(
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
    ]]
)

many_criteria_choice.print_criteries(
    criteries_quantitative,
    criteries_qualitative
)

many_criteria_choice.print_symbols()
sets = many_criteria_choice.get_sets(criteries_quantitative, criteries_qualitative)
many_criteria_choice.get_generalized_criteria(sets)
