import pandas as pd

res_catboost = pd.read_csv('ml/results/catboost.csv')
res_logreg = pd.read_csv('ml/results/log_reg.csv')
res_randomforest = pd.read_csv('ml/results/random_forest.csv')

overall = pd.concat([
    res_catboost, 
    res_logreg,
    res_randomforest,
], ignore_index=True).drop('Unnamed: 0', axis=1, errors='ignore')

overall.to_csv('ml/experiments.csv', index=False)
