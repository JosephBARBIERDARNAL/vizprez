import matplotlib.pyplot as plt
import pandas as pd
from highlight_text import ax_text

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/economic/economic.csv"
df = pd.read_csv(url)

max_usa = df.loc[df["country"] == "united states", "unemployment rate"].max()

us_color = "#ae2f2f"
japan_color = "#44487e"

fig, ax = plt.subplots()
fig.subplots_adjust(hspace=1)
ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
ax.set_facecolor("#fffaf4")
fig.set_facecolor("#fffaf4")
ax.tick_params(size=0)
ax.set_xticks([])
ax.set_ylim(0, 15.5)
ax.grid(axis="y", color="#dfdfdf", linewidth=0.4, zorder=2)

for country in df["country"].unique():
    subset = df[df["country"] == country]
    x = subset["date"]
    y = subset["unemployment rate"]

    if country == "united states":
        style = dict(color=us_color, zorder=10, lw=2.2)
    elif country == "japan":
        style = dict(color=japan_color, zorder=10, lw=2.2)
    else:
        style = dict(color="#b6b5b5", zorder=4, lw=0.8)
    ax.plot(x, y, **style)

text_style = dict(y=-0.8, ha="center", size=7, color="#b4b4b4")
ax.text(x="2020-01-01", s="Jan 2020", **text_style)
ax.text(x="2023-12-01", s="Dec 2023", **text_style)

ax_text(
    x="2020-07-01",
    y=13.7,
    s=f"The <USA> had a peak unemployment\nrate of <{max_usa}%> in April 2020.",
    highlight_textprops=[{"color": us_color, "weight": "bold"}, {"weight": "bold"}],
    size=9,
)

ax_text(
    x="2021-04-01",
    y=1.5,
    s="<Japan> has maintained a very low unemployment\nrate during the entire period.",
    highlight_textprops=[{"color": japan_color, "weight": "bold"}],
    size=9,
)

fig.text(x=0.5, y=0.94, s="Unemployment rates during COVID-19", ha="center", size=18)
fig.text(
    x=0.5,
    y=0.9,
    s="From January 2020 to December 2023",
    color="#b9b9b9",
    weight="light",
    ha="center",
    size=10,
)

plt.show()
