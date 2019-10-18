import pandas as pd
import pytest
from reframe import Relation


@pytest.fixture(scope="module")
def r():
    data_real = {"name": ["Carol", "Bob"], "age": [86, 4]}
    df = pd.DataFrame(data=data_real)
    return Relation(df)


def test_foo(r):
    r = r.extend("birth", 2019 - r.age).project(["name", "age", "birth"]).head(10)
    data_expected = {"name": ["Carol", "Bob"], "age": [86, 4], "birth": [1933, 2015]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)

    assert r.equals(r_expected)


def test_foo_2(r):
    r = r.extend("doublename", r.name + r.name).project(["doublename"]).head(10)
    r_expected_2 = Relation("tests/test_extent_expected_1.csv", sep="|")
    assert r.equals(r_expected_2)
