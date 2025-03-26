import calendar
import pandas as pd
import matplotlib.pyplot as plt
import morethemes as mt
import dayplot as dp

df = pd.read_csv("timeseries/elonmusk.csv")
df["Datetime"] = pd.to_datetime(df["Datetime"])
df["Date"] = df["Datetime"].dt.strftime("%Y-%m-%d")
df = df.groupby("Date").size().reset_index(name="n_tweets")
df = df[df["Date"] <= "2022-12-31"]
df = df[df["Date"] >= "2022-01-01"]

mt.set_theme("urban")

fig, ax = plt.subplots(figsize=(15, 5))

dp.calendar(
    dates=df["Date"],
    values=df["n_tweets"],
    start_date="2022-01-01",
    end_date="2022-12-31",
    cmap="Reds",
    edgecolor="black",
    edgewidth=0.5,
    mutation_scale=1.15,
    color_for_none="#000000",
    ax=ax,
)
fig.text(x=0.12, y=0.75, s="Total number of Elon Musk tweets in 2022", size=16)

fig.savefig("timeseries/calendar_heatmap_black.png", dpi=300, bbox_inches="tight")
