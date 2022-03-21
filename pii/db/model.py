from __future__ import annotations

from typing import List, Generic, TypeVar, Type

from peewee import Model

T = TypeVar("T")


class QueryBuild(Generic[T]):
    def __init__(self, value=T):
        self.model: Model = value

    def select(self, arr) -> QueryBuild[T]:
        return self

    def where(self, a) -> QueryBuild[T]:
        return self

    def orderBy(self, a) -> QueryBuild[T]:
        return self

    def limit(self, a) -> QueryBuild[T]:
        return self

    def one(self) -> T:
        one = self.model.select().get()
        return one

    def all(self) -> List[T]:
        arr = list(self.model.select())
        return arr


class PModel:
    _empty = False

    @classmethod
    def find(cls: Type[T]) -> QueryBuild[T]:
        """
        T https://stackoverflow.com/a/39205612/384617
        """
        return QueryBuild(cls)

    def setEmpty(self):
        self._empty = True

    def isPresent(self) -> bool:
        return not self._empty
