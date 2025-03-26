import calendar
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import morethemes as mt

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

mt.set_theme("urban")
plt.rcParams["axes.grid"] = False

df["month"] = df["Date"].dt.month
df["day"] = df["Date"].dt.day

heatmap_data = pd.pivot_table(
    df, values="n_tweets", index="day", columns="month", aggfunc="sum"
)

fig = plt.figure(figsize=(10, 10))

ax = sns.heatmap(
    heatmap_data,
    cmap="Reds",
    linewidths=0.5,
    linecolor="gray",
    cbar_kws={"label": "Number of Tweets"},
)

x_labels = [calendar.month_abbr[i] for i in range(1, 13)]
ax.set_xticklabels(x_labels)
ax.tick_params(labelsize=15)
fig.text(x=0.1, y=0.9, s="Total number of Elon Musk tweets in 2022", size=20)

fig.savefig("timeseries/heatmap2.png", dpi=300, bbox_inches="tight")
