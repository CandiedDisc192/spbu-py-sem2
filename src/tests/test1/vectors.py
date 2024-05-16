from __future__ import annotations

from typing import Any, Generic, Protocol, TypeVar


class ArithmeticAvailable(Protocol):
    def __add__(self, other: Any) -> Any:
        pass

    def __sub__(self, other: Any) -> Any:
        pass

    def __mul__(self, other: Any) -> Any:
        pass


T = TypeVar("T", bound=ArithmeticAvailable)


class VectorDimensionError(Exception):
    def __init__(self, message: str = "Vectors must have the same dimension") -> None:
        self.message = message
        super().__init__(self.message)


class VectorCrossProductError(VectorDimensionError):
    def __init__(self, message: str = "Cross product is only defined for 3D vectors") -> None:
        self.message = message
        super().__init__(self.message)


class Vector(Generic[T]):
    def __init__(self, elements: list[T]) -> None:
        self.dim = len(elements)
        self.elements = elements

    def __add__(self, other: Vector) -> Vector:
        if other.dim != self.dim:
            raise VectorDimensionError
        return Vector([self.elements[i] + other.elements[i] for i in range(self.dim)])

    def __sub__(self, other: Vector) -> Vector:
        if other.dim != self.dim:
            raise VectorDimensionError
        return Vector([self.elements[i] - other.elements[i] for i in range(self.dim)])

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and self.elements == other.elements

    def dot_product(self, other: Vector) -> float:
        if other.dim != self.dim:
            raise VectorDimensionError
        return sum([self.elements[i] * other.elements[i] for i in range(self.dim)])

    def cross_product(self, other: Vector) -> Vector:
        if self.dim != 3 or other.dim != 3:
            raise VectorCrossProductError
        ax, ay, az = self.elements
        bx, by, bz = other.elements
        return Vector([ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx])

    def is_zero(self) -> bool:
        return all([not i for i in self.elements])

    def dimension(self) -> int:
        return self.dim
