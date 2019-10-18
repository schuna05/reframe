import pandas as pd
import pytest
from reframe import Relation


#@pytest.fixture(scope="module")
def test_foo():
    df1 = Relation(pd.read_csv("tests/test_outer_join/test_outer_join_1.csv",sep="|"))
    df2 = Relation(pd.read_csv("tests/test_outer_join/test_outer_join_2.csv",sep="|"))
    df = df1.outerjoin(df2)
    df_expected = pd.read_csv("tests/test_outer_join/test_outer_join_3.csv")
    
    assert df.equals(df_expected)

def test_foo_2():
    df1 = Relation(pd.read_csv("tests/test_outer_join/test_outer_join_4.csv"))
    df2 = Relation(pd.read_csv("tests/test_outer_join/test_outer_join_5.csv"))

    
    df_expected = pd.read_csv("tests/test_outer_join/test_outer_join_6.csv")
    assert df.equals(df_expected)
