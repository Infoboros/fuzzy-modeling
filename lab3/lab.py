from lab3.accumulation import Accumulation, AccumulationProcessor
from lab3.activation import lB1, lB2, lB3, lB4, lB5, ActivateProcessor
from lab3.defuzzyficator import SimpleDeFuzzyficator
from lab3.fuzzyficator import SingletonFuzzyficator
from lab3.pred_activations import *

# Настройки
Fuzzyficator = SingletonFuzzyficator
implication = lambda x, y: min(1, 1 - x + y)
accumulation_funk = max
DeFuzzyficator = SimpleDeFuzzyficator

xs = [9, 2.5, 8, 5, 5]

print(f'Входные данные {", ".join([f"x{index + 1}={x}" for index, x in enumerate(xs)])}')
print()
print('1 Уровень - фаззификация')
As = [
    Fuzzyficator(criteria).fuzzy(x)
    for x, criteria in zip(
        xs,
        [A1(), A2(), A3(), A4(), A5()]
    )
]

print()
print('2 Уровень – активация (подусловия)')
Cs = [
    C1(As[0], implication),
    C2(As[3], implication),
    C3(As[0], implication),
    C4(As[1], implication),
    C5(As[2], implication),
    C6(As[0], implication),
    C7(As[3], implication),
    C8(As[1], implication),
    C9(As[2], implication),
    C10(As[4], implication),
    C11(As[0], implication),
    C12(As[3], implication),
    C13(As[1], implication),
    C14(As[2], implication),
    C15(As[0], implication),
    C16(As[3], implication),
    C17(As[1], implication),
    C18(As[2], implication),
    C19(As[4], implication),
]
processor = PreadActivationProcess(Cs)
result_Cs = processor.process()

print()
print('3 Уровень – активация (все правило)')
Bs = [
    lB1(result_Cs),
    lB2(result_Cs),
    lB3(result_Cs),
    lB4(result_Cs),
    lB5(result_Cs),
]
processor = ActivateProcessor(Bs)
result_Bs = processor.process()

print()
print('4 Уровень – Аккумуляция')
accumulation = Accumulation(result_Bs, accumulation_funk)
processor = AccumulationProcessor(accumulation)
result_accumulation = processor.process()

print()
print('5 Уровень – Деффузификация')
defuzzyficator = DeFuzzyficator(B1())
defuzzyficator.fuzzy(result_accumulation)
