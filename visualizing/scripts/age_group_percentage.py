import matplotlib.pyplot as plt
import polars as pl
import seaborn as sns

sns.set_style('whitegrid')
plt.style.use('visualizing/style.mplstyle')

df2020_raw = pl.read_csv('preprocessing/data/raw/heart_2020_cleaned.csv')

age_heart_rate_2020 = df2020_raw.with_columns(
    (pl.col('HeartDisease') == 'Yes').cast(pl.Int64).alias('HeartDisease')
).group_by('AgeCategory').agg(
    pl.len(),
    (pl.mean('HeartDisease') * 100).alias('Percent')
).sort('AgeCategory')

plt.figure(figsize=(8, 4))

ax = sns.barplot(
    x='AgeCategory',
    y='Percent',
    data=age_heart_rate_2020,
    color='#3ecd86',
)

# plt.title('1.3. Доля респондентов с CCЗ по возрастным категориям, набор 2020 года')
ax.bar_label(ax.containers[0], labels=[f'{value:.1f}\%' for value in age_heart_rate_2020['Percent']], padding=3)
plt.xlabel('Возрастная категория')
plt.ylabel('Доля больных ССЗ (\%)')
plt.xticks(rotation=15)
plt.savefig('visualizing/plots/age_group_percentage_2020.png', dpi=300)
