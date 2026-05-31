import matplotlib.pyplot as plt
import polars as pl
import seaborn as sns

sns.set_style('whitegrid')
plt.style.use('visualizing/style.mplstyle')

df2020_raw = pl.read_csv('preprocessing/data/raw/heart_2020_cleaned.csv')
df2022_raw = pl.read_csv('preprocessing/data/raw/heart_2022_with_nans.csv')

numerical2020 = [
    'BMI',
    'PhysicalHealth',
    'MentalHealth',
    'SleepTime'
]

fig, axes = plt.subplots(2, 2, figsize=(6, 8))
axes = axes.flatten()
for i, col in enumerate(numerical2020):
    sns.boxplot(df2020_raw[col], ax=axes[i], color='#3ecd86')
    axes[i].set_title(col)

fig.suptitle('Ящики с усами для числовых признаков, набор данных 2020 года')
fig.tight_layout()
plt.savefig('visualizing/plots/boxplot_outliers_2020.png', dpi=250)

numerical2022 = [
    'PhysicalHealthDays',
    'MentalHealthDays',
    'SleepHours',
    'WeightInKilograms',
    'BMI',
    'HeightInMeters'
]

fig, axes = plt.subplots(2, 3, figsize=(9, 8))
axes = axes.flatten()
for i, col in enumerate(numerical2022):
    sns.boxplot(df2022_raw[col], ax=axes[i], color='#3ecd86')
    axes[i].set_title(col)

fig.suptitle('Ящики с усами для числовых признаков, набор данных 2022 года')
fig.tight_layout()
plt.savefig('visualizing/plots/boxplot_outliers_2022.png', dpi=250)
