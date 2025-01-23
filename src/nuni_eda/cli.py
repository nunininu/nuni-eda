

from president_speech.db.parquet_interpreter import read_parquet, get_parquet_full_path
import pandas as pd

def group_by_count_temp(keyword:str, asc: bool = False, rcnt: int = 12):
    """
    지정한 keyword로 필터링하여 대통령별로 그룹화하고, count를 기준으로 정렬하여 데이터프레임으로 반환합니다.
    """
    #TODO: ascending , cnffur rows size
    #pytest 코드를 만들어 보세요
    #import this <-해석해보세요

    data_path = get_parquet_full_path()
    df = pd.read_parquet(data_path)
    fdf = df[df['speech_text'].str.contains(keyword, case=False)]
    gdf = fdf.groupby("president").size().reset_index(name="count")
    sdf = gdf.sort_values(by='count', ascending=asc).reset_index(drop=True)
    rdf = sdf.head(rcnt)
    return rdf

def print_group_by_count(keyword: str, asc: bool=False, rcnt: int=12):
    df = group_by_count(keyword, asc, rcnt)
    print(df.to_string(index=False))


def entry_point():
    typer.run(print_group_by_count)


def group_by_count(keyword:str, asc: bool = False, rcnt: int = 12, keyword_sum: bool=False):

    data_path = get_parquet_full_path()
    df = pd.read_parquet(data_path)
    fdf = df[df['speech_text'].str.contains(keyword, case=False)]

    if(keyword_sum):
       # fdf['keyword_sum']
       pass

    gdf = fdf.groupby("president").size().reset_index(name="count")
    sdf = gdf.sort_values(by='count', ascending=asc).reset_index(drop=True)
    rdf = sdf.head(rcnt)
    rdf['keyword_sum'] = '사표는 책상위에 두었습니다'
    return rdf

def print_group_by_count(keyword: str, asc: bool=False, rcnt: int=12):
    df = group_by_count(keyword, asc, rcnt)
    print(df.to_string(index=False))


