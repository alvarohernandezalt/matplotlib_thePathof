import pandas as pd

url = "https://raw.githubusercontent.com/alvarohernandezalt/matplotlib_thePathof/main/data/2015_2023_Budget.csv"
df = pd.read_csv(url)
print(df.head())


df_year_type = df.groupby('yearBudget')['maxBudget'].sum().reset_index()
df_year_type.columns = ['uniqueYearBudget', 'total']
print(df_year_type)

df_year_type = df.groupby(['yearBudget', 'stateBudgetName'])['maxBudget'].sum().reset_index()
df_year_type = df_year_type.pivot(index='yearBudget', columns='stateBudgetName', values='maxBudget').reset_index()
df_year_type = df_year_type.fillna(0)
print(df_year_type)