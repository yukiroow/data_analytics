# Dominguez, Harry
# 9463 - IT 322
# Prelim Activity 1
import pandas as panda
import numpy as np
import matplotlib.pyplot as mpl

resto_data = panda.read_csv("prelimact1/resto1.csv")

small_items = resto_data[resto_data["Size"] == "S"]
medium_items = resto_data[resto_data["Size"] == "M"]
large_items = resto_data[resto_data["Size"] == "L"]

# Small Items
smi_mean = small_items["Count"].mean()
smi_median = small_items["Count"].median()
smi_std = small_items["Count"].std()

# Medium Items
mdi_mean = medium_items["Count"].mean()
mdi_median = medium_items["Count"].median()
mdi_std = medium_items["Count"].std()

# Large Items
lgi_mean = large_items["Count"].mean()
lgi_median = large_items["Count"].median()
lgi_std = large_items["Count"].std()

# Display in Tabular Format
from prettytable import PrettyTable

statistical_table = PrettyTable()
statistical_table.title = "resto1.csv Statistics"
statistical_table.field_names = [
    " ",
    "Mean",
    "Median",
    "Standard Deviation (S)",
]
statistical_table.add_rows(
    [
        [
            "S",
            smi_mean,
            smi_median,
            smi_std,
        ],
        [
            "M",
            mdi_mean,
            mdi_median,
            mdi_std,
        ],
        ["L", lgi_mean, lgi_median, lgi_std],
    ]
)
print(statistical_table)

# Data Visualization
# Mean
bar_x = np.array(["S", "M", "L"])
bar_y = np.array([smi_mean, mdi_mean, lgi_mean])

mpl.figure(1)
mpl.title("Average Item Count per Item Size (Mean)")
mpl.xlabel("Item Size")
mpl.ylabel("Mean")
mpl.bar(bar_x, bar_y, width=0.3)

# Median
bar_y = np.array([smi_median, mdi_median, lgi_median])

mpl.figure(2)
mpl.title("Average Item Count per Item Size (Median)")
mpl.xlabel("Item Size")
mpl.ylabel("Median")
mpl.bar(bar_x, bar_y, width=0.3)

# Standard Deviation
points_y = np.array([smi_std, mdi_std, lgi_std])

mpl.figure(3)
mpl.title("Standard Deviation Count per Item Size")
mpl.xlabel("Item Size")
mpl.ylabel("Standard Deviation")
mpl.plot(bar_x, points_y)
mpl.text(bar_x[0], points_y[0], points_y[0])
mpl.text(bar_x[1], points_y[1], points_y[1])
mpl.text(bar_x[2], points_y[2], points_y[2])

mpl.show()
