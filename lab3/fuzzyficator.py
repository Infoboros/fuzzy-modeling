from criteria import Criteria
from utils import get_interval, get_normal


class Fuzzyficator:
    def __init__(self, criteria: Criteria):
        self.criteria = criteria


class SingletonFuzzyficator(Fuzzyficator):
    def fuzzy(self, x):
        interval = list(get_interval(self.criteria.range, self.criteria.step))
        print(f'`{self.criteria.code}={"{"}{" + ".join([ f"{1 if el == x else 0}/{el}" for el in interval])}{"}"}')
        return [
            (1 if el == x else 0)
            for el in interval
        ]


class NoneSingletonFuzzyficator(Fuzzyficator):
    def fuzzy(self, x):
        interval = list(get_interval(self.criteria.range, self.criteria.step))
        print(f'`{self.criteria.code}={"{"}{" + ".join([f"{get_normal(x, 0.5)(el)}/{el}" for el in interval])}{"}"}')
        return [
            get_normal(x, 0.5)(el)
            for el in interval
        ]