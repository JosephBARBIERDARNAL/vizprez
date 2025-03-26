from great_tables import GT
import pandas as pd

df = pd.read_csv("timeseries/elonmusk.csv")
df["Datetime"] = pd.to_datetime(df["Datetime"])
df["Date"] = df["Datetime"].dt.strftime("%Y-%m-%d")
df = df.groupby("Date").size().reset_index(name="n_tweets")
df = df[df["Date"] <= "2022-12-31"]
df = df[df["Date"] >= "2022-01-01"]
df["Date"] = pd.to_datetime(df["Date"])
full_date_range = pd.date_range(start=df["Date"].min(), end=df["Date"].max())
df = df.set_index("Date").reindex(full_date_range, fill_value=0).reset_index()
df.columns = ["Date", "n_tweets"]

gt_table = GT(df.head(10))
gt_table.save("elonmusk.png", scale=2, web_driver="firefox")
