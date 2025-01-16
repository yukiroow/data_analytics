# Dominguez, Harry
# 9463 - IT 322
# Prelim Activity 1
import pandas as panda

resto_data = panda.read_csv("prelimact1/resto1.csv")

small_items = resto_data[resto_data["Size"] == "S"]
medium_items = resto_data[resto_data["Size"] == "M"]
large_items = resto_data[resto_data["Size"] == "L"]

# Small Items
smi_mean = small_items["Count"].mean()
smi_median = small_items["Count"].median()
smi_mode = (
    None
    if small_items["Count"].size == small_items["Count"].mode().size
    else small_items["Count"].mode()
)
smi_var = small_items["Count"].var()
smi_std = small_items["Count"].std()

# Medium Items
mdi_mean = medium_items["Count"].mean()
mdi_median = medium_items["Count"].median()
mdi_mode = (
    None
    if medium_items["Count"].size == medium_items["Count"].mode().size
    else medium_items["Count"].mode()
)
mdi_var = medium_items["Count"].var()
mdi_std = medium_items["Count"].std()

# Large Items
lgi_mean = large_items["Count"].mean()
lgi_median = large_items["Count"].median()
lgi_mode = (
    None
    if large_items["Count"].size == large_items["Count"].mode().size
    else large_items["Count"].mode()
)
lgi_var = large_items["Count"].var()
lgi_std = large_items["Count"].std()

# Display in Tabular Format
from prettytable import PrettyTable

statistical_table = PrettyTable()
statistical_table.title = "resto1.csv Statistics"
statistical_table.field_names = [" ", "S", "M", "L"]
statistical_table.add_row(
    [
        "Mean",
        smi_mean,
        mdi_mean,
        lgi_mean,
    ]
)
statistical_table.add_row(
    [
        "Median",
        smi_median,
        mdi_median,
        lgi_median,
    ]
)
statistical_table.add_row(
    [
        "Modes",
        smi_mode.values.tolist(),
        mdi_mode.values.tolist(),
        lgi_mode,
    ]
)
statistical_table.add_row(
    [
        "Variance (P)",
        smi_var,
        mdi_var,
        lgi_var
    ]
)
statistical_table.add_row(
    [
        "Standard Deviation (P)",
        smi_std,
        mdi_std,
        lgi_std
    ]
)
print(statistical_table)