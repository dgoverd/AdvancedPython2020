import random


class ExcessSymbolError(Exception):
    pass


class DNA:
    def __init__(self, chain):  # вводим 1 цепь Днк, так как вторая комплиментарна, ее можем построить сами
        if not set(chain).issubset({'A', 'C', 'G',
                                    'T'}):  # set.issubset производит проверку, является ли рассматриваемое множество
            # подмножеством заданного
            raise ExcessSymbolError(
                'В введенной строке есть символы, не содержащиеся в ДНК')  # если лишняя буква - ошибка
        self.strand1 = chain
        self.strand2 = ''.join([{'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}[symbol] for symbol in
                                self.strand1])  # строим комплементарную цепь

    def __str__(self):  # создает строку из строк
        return str([self.strand1, self.strand2])

    def __repr__(self):
        return str([self.strand1, self.strand2])

    def __getitem__(self, i):  # поддерживает индексацию (по индексу возвращает пару азотистых оснований)
        return self.strand1[i], self.strand2[i]

    def __add__(self, another):  # сложение
        return DNA(self.strand1 + another.strand1)

    def __mul__(self, another):  # перемножение
        firstLength, secondLength = len(self.strand1), len(another.strand1)
        if firstLength > secondLength:
            end = self.strand1[-firstLength + secondLength:]
        else:
            end = another.strand1[-secondLength + firstLength:]
        return DNA(''.join(
            [random.choice([symbol1, symbol2]) for symbol1, symbol2 in zip(self.strand1, another.strand1)]) + end)

    def __eq__(self, another):  # проверка на равенство
        return self.strand1 == another.strand1 or self.strand1 == another.strand2


class RNA(str):
    def __init__(self, chain):
        super().__init__()
        if not set(chain).issubset({'A', 'C', 'G', 'U'}):  # проверка на лишние символы
            raise ExcessSymbolError(
                'В введенной строке есть символы, не содержащиеся в РНК')  # если лишний, выдаем ошибку
        self.rna = chain

    def __str__(self):  # создает строку из строк
        return self.rna

    def __repr__(self):
        return self.rna

    def __getitem__(self, i):  # поддерживает индексацию
        return self.rna[i]

    @property
    def getComplementaryDNA(self):  # строит комплементарную ДНК
        return DNA(''.join([{'A': 'T', 'U': 'A', 'G': 'C', 'C': 'G'}[symbol] for symbol in self.rna]))

    def __add__(self, another):  # сложение цепей
        return RNA(self.rna + another.rna)

    def __mul__(self, another):  # перемножение ДНК
        firstLength, secondLength = len(self.rna), len(another.rna)
        if firstLength > secondLength:
            end = self.rna[-firstLength + secondLength:]
        else:
            end = another.rna[-secondLength + firstLength:]
        print(''.join([random.choice([symbol1, symbol2]) for symbol1, symbol2 in zip(self.rna, another.rna)]) + end)
        return RNA(
            ''.join([random.choice([symbol1, symbol2]) for symbol1, symbol2 in zip(self.rna, another.rna)]) + end)

    def __eq__(self, another):  # проверка на равные
        return self.rna == another.rna
