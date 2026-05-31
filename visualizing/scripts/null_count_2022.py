import matplotlib.pyplot as plt
import polars as pl
import seaborn as sns

sns.set_style('whitegrid')
plt.style.use('visualizing/style.mplstyle')

df2022 = pl.read_csv('preprocessing/data/raw/heart_2022_with_nans.csv')
null_counts = df2022.null_count().transpose(
    include_header=True,
    header_name='Column',
    column_names=['NullCount']
).sort('NullCount', descending=True)

plt.figure(figsize=(8, 8))

ax = sns.barplot(
    null_counts,
    x='NullCount',
    y='Column',
    color='#3ecd86'
)

ax.bar_label(ax.containers[0], padding=3)
left, right = plt.xlim()
plt.xlim(right=right+4000)
plt.xlabel('Количество пропусков')
plt.ylabel('Признак')
plt.title('Кол-во пропущенных значений у каждого признака в наборе данных 2022 года')
plt.savefig('visualizing/plots/null_count_2022.png', dpi=250)
