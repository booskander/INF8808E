from preprocess import convert_dates, filter_years, summarize_yearly_counts, restructure_df, get_daily_info
import pandas as pd
data = pd.read_csv('assets/data/arbres.csv')

data = convert_dates(data)

data = restructure_df(summarize_yearly_counts(filter_years(data, 2010, 2020)))

print(data)
