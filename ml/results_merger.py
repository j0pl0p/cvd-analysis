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

fi_2020 = pd.read_csv('ml/results/feature_importance_2020.csv')
fi_2022 = pd.read_csv('ml/results/feature_importance_2022.csv')
fi_merged = pd.read_csv('ml/results/feature_importance_merged.csv')

fi_overall = pd.concat([
    fi_2020, 
    fi_2022,
    fi_merged,
], ignore_index=True)

fi_overall.to_csv('ml/feature_importances.csv', index=False)
