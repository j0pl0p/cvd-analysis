import polars as pl

BINARY_2020 = [
    'HeartDisease',
    'Smoking',
    'AlcoholDrinking',
    'Stroke',
    'DiffWalking',
    'PhysicalActivity',
    'Asthma',
    'KidneyDisease',
    'SkinCancer'
]

BINARY_2022 = [
    'PhysicalActivities', 'HadHeartAttack', 'HadAngina',
    'HadStroke', 'HadAsthma', 'HadSkinCancer',
    'HadCOPD', 'HadDepressiveDisorder', 'HadKidneyDisease',
    'HadArthritis', 'DeafOrHardOfHearing', 'BlindOrVisionDifficulty',
    'DifficultyConcentrating', 'DifficultyWalking', 'DifficultyDressingBathing',
    'DifficultyErrands', 'ChestScan', 'AlcoholDrinkers', 'HIVTesting',
    'FluVaxLast12', 'PneumoVaxEver', 'HighRiskLastYear',
]


def binarize_2020(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        (pl.col(BINARY_2020) == 'Yes')
        .cast(pl.Int64)
    )


def binarize_2022(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        (pl.col(BINARY_2022) == 'Yes')
        .cast(pl.Int64)
    )
