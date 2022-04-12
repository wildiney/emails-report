import pandas as pd
import numpy as np
from functools import reduce

main_df = pd.read_csv('mailing 261020.csv', sep=";", encoding="ANSI")

files = []


def clean_file(file):
    df = pd.read_csv(file + '.csv')
    df[file] = 1
    return df[['email', file]].drop_duplicates(subset="email")


cp00 = clean_file(files[0])
cp01 = clean_file(files[1])
cp02 = clean_file(files[2])
cp03 = clean_file(files[3])
cp04 = clean_file(files[4])
cp05 = clean_file(files[5])
cp06 = clean_file(files[6])
cp07 = clean_file(files[7])
cp08 = clean_file(files[8])
cp09 = clean_file(files[9])
cp10 = clean_file(files[10])
cp11 = clean_file(files[11])
cp12 = clean_file(files[12])

dfs = [main_df, cp00, cp01, cp02, cp03,
       cp04, cp05, cp06, cp07, cp08, cp09, cp10, cp11, cp12]

result = reduce(lambda x, y: pd.merge(x, y, on="email", how="outer"), dfs)
result = result.replace(np.nan, 0)
result.head()
result['Total'] = result[files[0]] + result[files[1]] + \
    result[files[2]] + result[files[3]] + \
    result[files[4]] + result[files[5]] + \
    result[files[6]] + result[files[7]] + \
    result[files[8]] + result[files[9]] + result[files[10]] + \
    result[files[11]] + result[files[11]]


df_nao_lidos = result[(result['Total'] == 0)].groupby(
    ['Area']).count()['Total']
df_lidos = result[(result['Total'] > 0)].groupby(
    ['Area']).count()['Total']
df_total = pd.merge(df_lidos, df_nao_lidos, how="outer", on="Area")
df_total.rename(columns={'Total_x': 'Leitores', 'Total_y': 'Nao_leitores'}, index={
                '0': 'E-Servicios'}, inplace=True)
df_total.fillna(0)

df_total["Porcentagem_leitores"] = df_total["Leitores"] * \
    100 / (df_total["Leitores"]+df_total["Nao_leitores"])

df_total


#result.to_excel("result.xlsx", encoding="utf-8")
