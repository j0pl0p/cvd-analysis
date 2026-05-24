import matplotlib.pyplot as plt
import polars as pl
import seaborn as sns

sns.set_style('whitegrid')
plt.style.use('visualizing/style.mplstyle')

df2020 = pl.read_csv('preprocessing/data/processed/df_2020_preprocessed.csv')
df2022 = pl.read_csv('preprocessing/data/processed/df_2022_preprocessed.csv')

stats_2020 = df2020.group_by('HeartDisease').agg(pl.len().alias('Count')).with_columns(
    pl.lit('2020').alias('Year'),
    (pl.col('Count') / pl.col('Count').sum() * 100).alias('Percent')
)

stats_2022 = df2022.group_by('HeartDisease').agg(pl.len().alias('Count')).with_columns(
    pl.lit('2022').alias('Year'),
    (pl.col('Count') / pl.col('Count').sum() * 100).alias('Percent')
)

plot_df = pl.concat([stats_2020, stats_2022]).with_columns(
    pl.when(pl.col('HeartDisease') == 0)
    .then(pl.lit('Здоровые'))
    .otherwise(pl.lit('Больные ССЗ'))
    .alias('HeartDisease')
)

plt.figure(figsize=(8, 4))
colors = ['#3ecd86', '#fd3b66']
ax = sns.barplot(
    data=plot_df,
    x='Year',
    y='Percent',
    hue='HeartDisease',
    palette=colors
)

for container in ax.containers:
    labels = [f'{bar.get_height():.2f}\%' for bar in container]
    ax.bar_label(container, labels=labels)

plt.xlabel('Год набора данных')
plt.ylabel('Доля респондентов (\%)')
plt.legend()

plt.tight_layout()
plt.savefig('visualizing/plots/target_imbalance_2020_2022_percent.png', dpi=300)
