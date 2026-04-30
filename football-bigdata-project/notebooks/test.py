import pandas as pd
df = pd.read_csv("data/football_stats_enriched.csv")
print(df["cluster_label"].value_counts())