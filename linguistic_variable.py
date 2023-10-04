class LinguisticVariable:
    def __init__(self, name: str, T: [str], I: [float], us: [dict]):
        self.name = name
        self.T = T
        self.I = I
        self.us = us

    def _get_str_T(self):
        return ', '.join([f'"{t}"' for t in self.T])

    def print(self):
        print(f'<"{self.name},T,[{self.I[0]};{self.I[-1]}],G,M">')
        print(f'T={"{" + self._get_str_T() + "}"}')
        print(f'I={"{" + "; ".join(list(map(str, self.I))) + "}"}')

        for index, t in enumerate(self.T):
            print(f'T{index+1} = "{t}", {self.us[index]["str"]}')
