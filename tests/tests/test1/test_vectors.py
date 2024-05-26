import pytest

from src.tests.test1.vectors import Vector, VectorCrossProductError, VectorDimensionError


@pytest.mark.parametrize(
    "elements1,elements2,expected",
    [
        ([20, 89, 19], [3, 23, 13], [23, 112, 32]),
        ([1], [1], [2]),
        ([32, 32], [1, 1], [33, 33]),
        ([-10.12, 20.19, -2.1, 23.33], [-10.1, 1.0, 2.1, 0.67], [-20.22, 21.19, 0.0, 24.0]),
        ([0], [0], [0]),
    ],
)
def test_add(elements1, elements2, expected):
    assert Vector(elements1) + Vector(elements2) == Vector(expected)


@pytest.mark.parametrize(
    "elements1,elements2,expected",
    [
        ([1, 1, 1], [0, -1, 1], [1, 2, 0]),
        ([20.0, 30.3], [20.0, -30.7], [0.0, 61.0]),
        ([0], [0], [0]),
        ([0], [-1.0], [1.0]),
        ([1324345, 21442, 2143], [100, 100, 100], [1324245, 21342, 2043]),
    ],
)
def test_sub(elements1, elements2, expected):
    assert Vector(elements1) - Vector(elements2) == Vector(expected)


@pytest.mark.parametrize(
    "elements1,elements2,expected",
    [
        ([2, 2], [2, 2, 2], False),
        ([11.11], [11.11], True),
        ([3, 3], [3.0, 3.0], True),
        ([-1.1], [-1.1], True),
        ([1, 2], [2, 1], False),
    ],
)
def test_eq(elements1, elements2, expected):
    assert (Vector(elements1) == Vector(elements2)) == expected


@pytest.mark.parametrize(
    "elements1,elements2,expected",
    [
        ([1, 2, 3], [4, 5, 6], 32),
        ([0, 0, 0], [1, 2, 3], 0),
        ([1, 1, 1], [1, 1, 1], 3),
        ([1.5, 2.5, 3.5], [1.5, 2.5, 3.5], 20.75),
        ([1, 2, 3], [-1.0, -2.0, -3.0], -14),
        ([7, 7, 7, 7, 7], [2, 3, 4, 5, 10002], 70112),
    ],
)
def test_dot_product(elements1, elements2, expected):
    assert Vector(elements1).dot_product(Vector(elements2)) == expected


@pytest.mark.parametrize(
    "elements1,elements2,expected",
    [
        ([1231, 53253, 35], [329, 421, 234], [12446467, -276539, -17001986]),
        ([1.5, 3.0, 1.0], [10, -1, 4], [13, 4, -31.5]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([5, 5, 5], [5, 2, 3], [5, 10, -15]),
    ],
)
def test_cross_product(elements1, elements2, expected):
    assert Vector(elements1).cross_product(Vector(elements2)) == Vector(expected)


@pytest.mark.parametrize(
    "elements,expected", [([0, 0, 0], True), ([0, 1], False), ([0.0, 0.0], True), ([0.0, 123132.12], False)]
)
def test_is_zero(elements, expected):
    assert Vector(elements).is_zero() == expected


@pytest.mark.parametrize("elements,expected", [([1, 2, 3], 3), ([1, 2], 2), ([1], 1), ([1.1], 1)])
def test_dimension(elements, expected):
    assert Vector(elements).dimension() == expected


@pytest.mark.parametrize(
    "elements1,elements2", [([0], [0, 2]), ([0.1, 1.1], [0.2, 0.3, 0.4]), ([0], [0, 0, 0, 0, 0, 0, 0, 0])]
)
def test_add_error(elements1, elements2):
    with pytest.raises(VectorDimensionError):
        Vector(elements1) + Vector(elements2)


@pytest.mark.parametrize(
    "elements1,elements2", [([0], [0, 2]), ([0.1, 1.1], [0.2, 0.3, 0.4]), ([0], [0, 0, 0, 0, 0, 0, 0, 0])]
)
def test_sub_error(elements1, elements2):
    with pytest.raises(VectorDimensionError):
        Vector(elements1) - Vector(elements2)


@pytest.mark.parametrize("elements1,elements2", [([0], [0, 2]), ([0.1, 1.1], [0.2, 0.3, 0.4]), ([1, 1], [9])])
def test_dot_product_error(elements1, elements2):
    with pytest.raises(VectorDimensionError):
        Vector(elements1).dot_product(Vector(elements2))


@pytest.mark.parametrize(
    "elements1,elements2",
    [([0, 1, 2, 3], [0, 2, 1, 4]), ([0.1, 1.1], [0.2, 0.3, 0.4]), ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5])],
)
def test_cross_product_error(elements1, elements2):
    with pytest.raises(VectorDimensionError):
        Vector(elements1).cross_product(Vector(elements2))
