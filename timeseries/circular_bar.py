import calendar
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

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="polar")

df["day_of_year"] = df["Date"].dt.dayofyear
df["angle"] = df["day_of_year"] * 2 * np.pi / 366

df["month"] = df["Date"].dt.month
df["month_name"] = df["Date"].dt.strftime("%b")

colors = cm.hsv(np.linspace(0, 1, 13))
month_colors = {i + 1: colors[i] for i in range(12)}

for month in range(1, 13):
    month_data = df[df["month"] == month]
    ax.plot(
        month_data["angle"],
        month_data["n_tweets"],
        color="#D61C20",
        alpha=0.7,
    )
    ax.scatter(
        month_data["angle"],
        month_data["n_tweets"],
        color="#D61C20",
        edgecolor="black",
        alpha=0.7,
        s=40,
    )

ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi / 2.0)
ax.set_xticks(np.linspace(0, 2 * np.pi, 13)[:-1])  # 12 months
ax.set_xticklabels(calendar.month_abbr[1:])
ax.tick_params(labelsize=15)
fig.text(x=0.1, y=0.93, s="Total number of Elon Musk tweets in 2022", size=18)

fig.savefig("timeseries/circular_bar.png", dpi=300, bbox_inches="tight")
