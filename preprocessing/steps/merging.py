import polars as pl


def merge_2020_and_2022(df2020: pl.DataFrame, df2022: pl.DataFrame) -> pl.DataFrame:
    # проверка что все признаки из 2020 года нашлись и в 2022
    assert df2020.shape[1] == len(set(df2020.columns) & set(df2022.columns))
    return pl.concat(
        [df2020.with_columns(pl.lit(2020).alias('Year')),
         df2022[df2022.columns].with_columns(pl.lit(2022).alias('Year'))],
        how='align'
    )
