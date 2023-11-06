from criteria import Criteria
from utils import get_interval


class DeFuzzyficator:
    def __init__(self, criteria: Criteria):
        self.criteria = criteria


class SimpleDeFuzzyficator(DeFuzzyficator):
    def fuzzy(self, x):
        result = sum(
            map(
                lambda row: row[0] * row[1],
                zip(x, self.criteria.interval)
            )
        ) / sum(x)
        print(
            f'b= ({" + ".join([f"{left}*{right}" for left, right in zip(x, list(self.criteria.interval))])}) / {sum(x)} = {result}')
