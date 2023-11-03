from criteria import Criteria
from utils import get_interval


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