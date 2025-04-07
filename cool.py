import matplotlib.pyplot as plt
import pandas as pd
from highlight_text import ax_text

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/economic/economic.csv"
df = pd.read_csv(url)

max_usa = df.loc[df["country"] == "united states", "unemployment rate"].max()


fig, ax = plt.subplots()

for country in df["country"].unique():
    subset = df[df["country"] == country]
    x = subset["date"]
    y = subset["unemployment rate"]
    ax.plot(x, y, label=country)

ax.legend()
fig.text(x=0.5, y=1, s="Unemployment rates during COVID-19")
