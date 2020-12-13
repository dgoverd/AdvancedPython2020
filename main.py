from _collections_abc import MutableMapping
from typing import _KT, _VT_co, _VT_co, Iterator, _T_co


class Dict(MutableMapping):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
    
    def __iter__(self) -> Iterator[_T_co]:
        pass

    def __len__(self) -> int:
        pass

    def __getitem__(self, k: _KT) -> _VT_co:
        pass

    def __delitem__(self, v: _KT) -> None:
        pass

    def __setitem__(self, k: _KT, v: _VT_co) -> None:
        pass
    
    
if __name__ == '__main__':
    pass
