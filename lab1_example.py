from alternatives import Alternatives
from criteria import FuzzyCriteria, QualitativeCriteria
from utils import get_normal

criteries_quantitative = [
    FuzzyCriteria(
        'Стоимость',
        get_normal(1500, 300),
        (600, 2400),
        1
    ),
    FuzzyCriteria(
        'Длина распространения сигнала',
        get_normal(0, 30),
        (0, 30),
        0.1
    ),
    FuzzyCriteria(
        'Пропускная способность',
        get_normal(0, 300),
        (0, 350),
        0.1
    ),
    FuzzyCriteria(
        'Количество VLAN портов',
        get_normal(0, 6),
        (0, 6),
        0.1
    ),
    FuzzyCriteria(
        'Вес',
        get_normal(150, 750),
        (150, 750),
        0.1
    ),
]
criteries_qualitative = [QualitativeCriteria('Известность бренда')]

criteries = criteries_quantitative + criteries_qualitative

alternatives = Alternatives(
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

alternatives.print_criteries(
    criteries_quantitative,
    criteries_qualitative
)

alternatives.print_symbols()
sets = alternatives.get_sets(criteries_quantitative)
