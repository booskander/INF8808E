from preprocess import summarize_lines, replace_others, clean_names
import pandas as pd
dataframe = pd.read_csv('./assets/data/romeo_and_juliet.csv')

df = summarize_lines(dataframe)


df = replace_others(df)


df = clean_names(df)

print(df)
