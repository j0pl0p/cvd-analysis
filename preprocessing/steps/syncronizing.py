import polars as pl

TO_RENAME_2020 = {
    'AlcoholDrinking': 'AlcoholDrinkers',
    'Asthma': 'HadAsthma',
    'Diabetic': 'HadDiabetes',
    'DiffWalking': 'DifficultyWalking',
    'GenHealth': 'GeneralHealth',
    'KidneyDisease': 'HadKidneyDisease',
    'MentalHealth': 'MentalHealthDays',
    'PhysicalActivity': 'PhysicalActivities',
    'PhysicalHealth': 'PhysicalHealthDays',
    'Race': 'RaceEthnicityCategory',
    'SkinCancer': 'HadSkinCancer',
    'SleepTime': 'SleepHours',
    'Smoking': 'SmokerStatus',
    'Stroke': 'HadStroke',
}


def rename_columns_2020(df: pl.DataFrame) -> pl.DataFrame:
    return df.rename(TO_RENAME_2020)


def binarize_smoker_status_2022(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.when(pl.col('SmokerStatus').is_in(
            ['Current smoker - now smokes every day', 'Current smoker - now smokes some days']))
        .then(pl.lit(1))
        .when(pl.col('SmokerStatus').is_in(['Former smoker', 'Never smoked']))
        .then(pl.lit(0))
        .otherwise(pl.lit(None)).cast(pl.Int64)
        .alias('SmokerStatus')
    )


def rename_values_2022(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns([
        pl.col('AgeCategory')
        .str.replace('Age ', '')
        .str.replace(' to ', '-')
        .alias('AgeCategory'),

        pl.when(pl.col('HadDiabetes') ==
                'No, pre-diabetes or borderline diabetes')
        .then(pl.lit('No, borderline diabetes'))
        .when(pl.col('HadDiabetes') == 'Yes, but only during pregnancy (female)')
        .then(pl.lit('Yes (during pregnancy)'))
        .otherwise(pl.col('HadDiabetes'))
        .alias('HadDiabetes'),

        pl.when(pl.col('RaceEthnicityCategory') == 'White only, Non-Hispanic')
        .then(pl.lit('White'))
        .when(pl.col('RaceEthnicityCategory') == 'Black only, Non-Hispanic')
        .then(pl.lit('Black'))
        .when(pl.col('RaceEthnicityCategory') == 'Hispanic')
        .then(pl.lit('Hispanic'))
        .when(pl.col('RaceEthnicityCategory').is_in(['Other race only, Non-Hispanic', 'Multiracial, Non-Hispanic']))
        .then(pl.lit('Other'))
        .otherwise(pl.lit(None))
        .alias('RaceEthnicityCategory')
    ])
