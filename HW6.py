class Dict:
    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)

    def __iter__(self):
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __delitem__(self, key) -> None:
        del self._data[key]

    def __setitem__(self, key, value) -> dict:
        self._data[key] = value

        return self._data

    def __add__(self, other):
        if isinstance(other, (Dict, dict)):
            for key in other:
                self[key] = other[key]

            return Dict(self._data)

        else:
            return NotImplemented

    def add(self, other):
        return self + other

    def __repr__(self):

        return str(self._data)

    @staticmethod
    def from_dict(dictionary):
        if isinstance(dictionary, dict):
            return Dict(dictionary)
        else:
            return ValueError


def test():
    a = Dict({'g': 7})
    a[6] = 7
    a['b'] = 18
    print(a)
    print(Dict(color='red', state='aggressive', time='123123'))
    print(Dict.from_dict({'time': '1:21', 'doing': 'writing hw'}))
    print(Dict(color='red', state='aggressive', time='123123')
          + Dict.from_dict({'time': '1:21', 'doing': 'writing hw', 'color': 'blue'}))
    print(Dict({'time': '1:21', 'doing': 'writing hw'}))
    print(type(a))


if __name__ == '__main__':
    test()
