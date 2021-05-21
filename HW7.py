import random


class ExcessSymbolError(Exception):
    pass


class NuclearAcid:
    def __init__(self, chain: str):
        self.bases_sequence = chain

    def __add__(self, other):
        return NuclearAcid(self.bases_sequence + other.bases_sequence)

    def __mul__(self, other):  # перемножение
        first_length, second_length = len(self.bases_sequence), len(other.bases_sequence)
        if first_length > second_length:
            tail = self.bases_sequence[-first_length + second_length:]
        else:
            tail = other.bases_sequence[-second_length + first_length:]
        return NuclearAcid(''.join(
            [random.choice([symbol1, symbol2]) for symbol1, symbol2 in
             zip(self.bases_sequence, other.bases_sequence)]) + tail)

    def __repr__(self):
        return str(self.bases_sequence)

    def __getitem__(self, item):  # поддерживает индексацию
        return self.bases_sequence[item]

    def __eq__(self, other):  # проверка на равные
        return self.bases_sequence == other.bases_sequence

    @property
    def complementedSequence(self, __complemented_bases={'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}):
        return NuclearAcid(''.join([__complemented_bases[symbol] for symbol in self.bases_sequence]))


class DNA(NuclearAcid):
    def __init__(self, chain, __set_of_bases={'A', 'T', 'G',
                                              'C'}):  # понимаю, что ставить изменияемые величины по умолчанию в функции
        # плохо, но мы не производим никаких действий по их изменению
        if not set(chain).issubset(__set_of_bases):
            raise ExcessSymbolError(
                'В введенной строке есть символы, не содержащиеся в ДНК')

        self.bases_sequence = NuclearAcid(chain)
        self.complemented_bases_sequence = NuclearAcid(chain).complementedSequence

    def __repr__(self):
        return str([self.bases_sequence, self.complemented_bases_sequence])

    def __getitem__(self, item):  # поддерживает индексацию
        return self.bases_sequence[item], self.complemented_bases_sequence[item]

    def __add__(self, other):
        return DNA(self.bases_sequence + other.bases_sequence)

    def __mul__(self, other):
        return DNA(self.bases_sequence * other.bases_sequence)

    def __eq__(self, other):  # проверка на равенство
        return (self.bases_sequence == other.bases_sequence
                or self.bases_sequence == other.complemented_bases_sequence)


class RNA(NuclearAcid):

    def __init__(self, chain, __set_of_bases={'A', 'U', 'G', 'C'},
                 ):
        if not set(chain).issubset(__set_of_bases):
            raise ExcessSymbolError(
                'В введенной строке есть символы, не содержащиеся в ДНК')

        NuclearAcid.__init__(self, chain)

    @property
    def getComplementaryDNA(self):  # строит комплементарную ДНК
        complemented_bases = {'A': 'T', 'U': 'A', 'G': 'C', 'C': 'G'}
        return DNA(''.join([complemented_bases[symbol] for symbol in self.bases_sequence]
                           )
                   )
