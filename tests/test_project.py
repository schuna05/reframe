import pandas as pd
from reframe import Relation


def r():
    data_real = {"name" : ["Alice","Bob","Carol"], "age" : [86,4,37]}
    df = pd.DataFrame(data=data_real)
    return Relation(df)

def test_foo():
    data_real = {"name": ["Carol", "Bob"], "age": [86, 4]}
    data_expected = {"name": ["Carol", "Bob"]}
    df = pd.DataFrame(data=data_real)
    df_expected = pd.DataFrame(data=data_expected)
    r = Relation(df)
    r_expected = Relation(df_expected)
    r_expected_2 = Relation('tests/test_project_expected_1.csv', sep='|')
    r2 = r.project(["name"])
    assert r2.equals(r_expected)
    assert r2.equals(r_expected_2)
