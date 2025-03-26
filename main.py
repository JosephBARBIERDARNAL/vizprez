from great_tables import GT
import pandas as pd

df = pd.DataFrame(
    {
        "categorie": [
            "transport",
            "transport",
            "transport",
            "alimentation",
            "alimentation",
            "alimentation",
            "alimentation",
            "alimentation",
            "alimentation",
        ],
        "source": [
            "voiture",
            "avion",
            "autres",
            "viande",
            "lait et oeufs",
            "fruits/légumes",
            "boissons",
            "poisson",
            "autres",
        ],
        "valeur": [
            2030,
            430,
            190,
            920,
            390,
            240,
            450,
            120,
            230,
        ],
    }
)

gt_table = GT(df)
gt_table.save("table.png", scale=2, web_driver="firefox")
