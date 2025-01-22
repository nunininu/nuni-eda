from nuni_eda.cli import group_by_count
import pandas as pd



def test_search_exception():
    row_count = 13
    df = group_by_count(keyword="자유", asc=True, rcnt=row_count)
    
    # assert
    assert isinstance(df, pd.DataFrame)
    assert len(df) < row_count

def test_default_args():
    # given
    # when
    #df = group_by_count(keyword="자유")
    df = group_by_count("자유")

    # then
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 12
    assert df.iloc[0]["president"] == "박정희"
    assert df.iloc[0]["count"] == 513
    assert df.iloc[1]["count"] == 438
    assert df.iloc[11]["count"] == 1
