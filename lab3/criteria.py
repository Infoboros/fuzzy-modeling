from utils import get_normal


class Criteria:
    def __init__(self, range: (int, int), step: float, func, name):
        self.range = range
        self.step = step
        self.func = func
        self.name = name

    @property
    def code(self):
        return f'A{str(self.__class__).split("A")[1][0]}'


class A1(Criteria):
    def __init__(self):
        super().__init__((9, 15), 1, get_normal(9, 2), 'Небольшое время формирования четверостишия')


class A2(Criteria):
    def __init__(self):
        super().__init__((2, 5), 0.5, get_normal(2, 1), 'Быстрый процесс обучения')


class A3(Criteria):
    def __init__(self):
        super().__init__((0, 10), 1, get_normal(10, 2), 'Большое количество настроечных параметров')


class A4(Criteria):
    def __init__(self):
        super().__init__((0, 5), 1, get_normal(5, 1), 'Высокое качество стихотворного текста')


class A5(Criteria):
    def __init__(self):
        super().__init__((0, 5), 1, get_normal(5, 2), 'Поддержка большинства языков программирования')


class Al1(Criteria):
    def __init__(self):
        super().__init__((9, 15), 1, lambda x: 1 - get_normal(9, 2)(x), 'Большое время формирования четверостишия')


class Al2(Criteria):
    def __init__(self):
        super().__init__((2, 5), 0.5, lambda x: 1 - get_normal(2, 1)(x), 'Медленный процесс обучения')


class Al3(Criteria):
    def __init__(self):
        super().__init__((0, 10), 1, lambda x: 1 - get_normal(10, 2)(x), 'Малое количество настроечных параметров')


class Al4(Criteria):
    def __init__(self):
        super().__init__((0, 5), 1, lambda x: 1 - get_normal(5, 1)(x), 'Низкое качество стихотворного текста')


class Al5(Criteria):
    def __init__(self):
        super().__init__((0, 5), 1, lambda x: 1 - get_normal(5, 2)(x), 'Плохая поддержка языков программирования')
