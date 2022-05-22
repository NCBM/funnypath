"""
A weird path implement for Python.
"""

import os
from typing import List, Optional, Union


class Path:
    def __init__(
        self,
        path: Optional[Union[str, "Path"]] = None,
        /,
        sep: str = os.path.sep
    ):
        self._paths: List[str] = []
        self._sep = sep
        if isinstance(path, str):
            self._paths.extend(path.split(sep))
        elif isinstance(path, Path):
            self._paths = path._paths

    def __str__(self):
        return self._sep.join(self._paths)

    def __repr__(self):
        return f"Path(\"{self.__str__()}\")"

    def __fspath__(self):
        return self.__str__()

    def __truediv__(self, key):
        _path = Path(sep=self._sep)
        _path._paths = self._paths + Path(key)._paths
        return _path

    def __mul__(self, key):
        _path = Path()
        _path._paths = self._paths.copy()
        _path._paths.reverse()
        if isinstance(key, str):
            key = Path(key, sep=self._sep)
        if not isinstance(key, Path):
            raise TypeError
        for seg in key._paths:
            _path._paths.remove(seg)
        _path._paths.reverse()
        return _path
