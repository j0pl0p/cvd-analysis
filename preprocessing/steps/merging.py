import polars as pl


def merge_2020_and_2022(df2020: pl.DataFrame, df2022: pl.DataFrame) -> pl.DataFrame:
    return pl.concat(
        [df2020.with_columns(pl.lit(2020).alias('Year')),
         df2022.with_columns(pl.lit(2022).alias('Year'))],
        how='diagonal'
    )
