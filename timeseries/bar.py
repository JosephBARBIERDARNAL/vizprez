import calendar
import pandas as pd
import matplotlib.pyplot as plt
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

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(df["Date"], df["n_tweets"])
x_ticks = [f"2022-{i + 1:02d}-01" for i in range(12)]
month_names = [calendar.month_name[i][:3] for i in range(1, 13)]
ax.set_xticks(x_ticks, labels=month_names)
ax.tick_params(labelsize=12)
fig.text(x=0.1, y=0.92, s="Total number of Elon Musk tweets in 2022", size=14)

fig.savefig("timeseries/bar.png", dpi=300, bbox_inches="tight")
