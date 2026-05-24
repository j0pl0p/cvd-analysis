import polars as pl

from steps.binarizing import binarize_2020, binarize_2022
from steps.clearing_data import (
    remove_target_nulls,
    remove_nonsense_2022,
    remove_nonsense_2020,
    remove_outliers_2020,
    remove_outliers_2022,
)
from steps.creating_target import create_target_2022
from steps.syncronizing import (
    binarize_smoker_status_2022,
    rename_columns_2020,
    rename_values_2022,
)
from steps.merging import merge_2020_and_2022

df2020_raw = pl.read_csv('preprocessing/data/raw/heart_2020_cleaned.csv')
df2022_raw = pl.read_csv('preprocessing/data/raw/heart_2022_with_nans.csv')

history_2020 = []
history_2022 = []


def process_2020(df: pl.DataFrame) -> tuple[pl.DataFrame, list]:
    history = [('Изначальный размер', len(df))]

    df_binarized = binarize_2020(df)
    history.append(('Бинаризация признаков', len(df_binarized)))

    df_no_outliers = remove_outliers_2020(df_binarized)
    history.append(('Удаление выбросов', len(df_no_outliers)))

    df_no_nonsense = remove_nonsense_2020(df_no_outliers)
    history.append(('Удаление противоречащих данных', len(df_no_nonsense)))

    df_renamed = rename_columns_2020(df_no_nonsense)
    history.append(('Переименование признаков', len(df_renamed)))

    return df_renamed, history


def process_2022(df: pl.DataFrame) -> tuple[pl.DataFrame, list]:
    history = [('Изначальный размер', len(df))]

    df_binarized = binarize_2022(df)
    history.append(('Бинаризация признаков', len(df_binarized)))

    df_with_target = create_target_2022(df_binarized)
    history.append(('Создание целевой переменной', len(df_with_target)))

    df_removed_nulls = remove_target_nulls(df_with_target)
    history.append(
        ('Удаление строк без целевой переменной', len(df_removed_nulls)))

    df_no_outliers = remove_outliers_2022(df_removed_nulls)
    history.append(('Удаление выбросов', len(df_no_outliers)))

    df_no_nonsense = remove_nonsense_2022(df_no_outliers)
    history.append(('Удаление противоречащих данных', len(df_no_nonsense)))

    df_smoker_binarized = binarize_smoker_status_2022(df_no_nonsense)
    history.append(('Бинаризация статуса курения', len(df_smoker_binarized)))

    df_renamed = rename_values_2022(df_smoker_binarized)
    history.append(('Переименование значений', len(df_renamed)))

    return df_renamed, history


processed_2020, history_2020 = process_2020(df2020_raw)
processed_2022, history_2022 = process_2022(df2022_raw)

df_merged = merge_2020_and_2022(processed_2020, processed_2022)

print('Обработка 2020 года:')
for i, h in enumerate(history_2020):
    print(
        f'{i + 1}. {h[0]}: {h[1]}, итого -{100 * (history_2020[0][1] - h[1]) / history_2020[0][1]:.2f}%')

print('\nОбработка 2022 года:')
for i, h in enumerate(history_2022):
    print(
        f'{i + 1}. {h[0]}: {h[1]}, итого -{100 * (history_2022[0][1] - h[1]) / history_2022[0][1]:.2f}%')

print(f'\nРазмер объединённого датасета: {len(df_merged)}')

processed_2020.write_csv(
    'preprocessing/data/processed/df_2020_preprocessed.csv', separator=',')
processed_2022.write_csv(
    'preprocessing/data/processed/df_2022_preprocessed.csv', separator=',')
df_merged.write_csv(
    'preprocessing/data/processed/df_merged.csv', separator=',')
