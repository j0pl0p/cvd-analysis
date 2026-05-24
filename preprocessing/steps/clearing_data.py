import polars as pl


def remove_target_nulls(df: pl.DataFrame) -> pl.DataFrame:
    return df.drop_nulls(['HeartDisease'])


def remove_outliers_2020(df: pl.DataFrame) -> pl.DataFrame:
    return df.filter(
        (pl.col('BMI').is_between(15, 60)) &
        (pl.col('SleepTime').is_between(3, 12))
    )


def remove_outliers_2022(df: pl.DataFrame) -> pl.DataFrame:
    return df.filter(
        (pl.col('BMI').is_between(15, 60)) &
        (pl.col('SleepHours').is_between(3, 12)) &
        (pl.col('WeightInKilograms').is_between(40, 160)) &
        (pl.col('HeightInMeters').is_between(1.4, 2.2))
    )


def remove_nonsense_2020(df: pl.DataFrame) -> pl.DataFrame:
    return df.filter(~(
        (pl.col('Sex') == 'Male') &
        (pl.col('Diabetic') == 'Yes (during pregnancy)')
    ))


def remove_nonsense_2022(df: pl.DataFrame) -> pl.DataFrame:
    df_no_pregnant_males = df.filter(~(
        (pl.col('Sex') == 'Male') &
        (pl.col('HadDiabetes') == 'Yes, but only during pregnancy (female)')
    ))

    return df_no_pregnant_males.filter(
        (pl.col('WeightInKilograms') /
         pl.col('HeightInMeters')**2 - pl.col('BMI')).abs() < 1
    )
