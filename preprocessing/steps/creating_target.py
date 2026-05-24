import polars as pl


def create_target_2022(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        ((pl.col('HadAngina') == 1) | (pl.col('HadHeartAttack') == 1))
        .cast(pl.Int64)
        .alias('HeartDisease')
    )
