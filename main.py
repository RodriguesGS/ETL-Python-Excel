import pandas as pd

from ydata_profiling import ProfileReport

df = pd.read_csv('data.csv')
profile = ProfileReport(df, title="Relatório de Análise")
profile.to_file("output.html")