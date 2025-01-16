# Dominguez, Harry
# 9463 - IT 322
# Prelim Activity 1
import pandas as panda
import matplotlib.pyplot as mpl
import numpy as np

sample_data = panda.read_csv("prelimact1/SAMPLE.csv")

sample_mean = sample_data["AGE"].mean()

sample_median = sample_data["AGE"].median()

sample_mode = sample_data["AGE"].mode()

# Average Ages per Year Level to be used for Standard Deviation and Variation
average_age_year1 = sample_data[sample_data["YEAR"] == 1][
    "AGE"
].mean()  # Filter to only 1st years
average_age_year2 = sample_data[sample_data["YEAR"] == 2][
    "AGE"
].mean()  # Filter to only 2nd years
average_age_year3 = sample_data[sample_data["YEAR"] == 3][
    "AGE"
].mean()  # Filter to only 3rd years
average_age_year4 = sample_data[sample_data["YEAR"] == 4][
    "AGE"
].mean()  # Filter to only 4th years

average_ages = panda.Series(
    [average_age_year1, average_age_year2, average_age_year3, average_age_year4]
)

sample_std = average_ages.std(ddof=0)  # Population Standard Deviation

sample_var = average_ages.var(ddof=0)  # Population Variation

# Display in Tabular Format
from prettytable import PrettyTable
statistical_table = PrettyTable()
statistical_table.title = "SAMPLE.csv Statistics"
statistical_table.field_names = ["Mean", "Median", "Modes", "Variance (P)", "Standard Deviation (P)"]
statistical_table.add_row([sample_mean, sample_median, sample_mode.values.tolist(), sample_var, sample_std])
print(statistical_table)

# Data Visualization

# Mean and Median
first_element = sample_data["NAME"][0]
last_element = sample_data["NAME"][9]

bar_x = np.array(sample_data["NAME"])
bar_y = np.array(sample_data["AGE"])
median_points_x = [first_element, last_element]
median_points_y = [sample_median, sample_median]
mean_points_x = [first_element, last_element]
mean_points_y = [sample_mean, sample_mean]

mpl.figure(1)
mpl.title("Mean and Median Age of Sample Students")
mpl.xlabel("Students")
mpl.ylabel("Ages")

mpl.bar(bar_x, bar_y, width = 0.3)
mpl.plot(median_points_x, median_points_y, color = "red", label = "Median Age")
mpl.plot(mean_points_x, mean_points_y, color = "yellow", label = "Mean Age")

mpl.legend()


# Mode
from matplotlib.lines import Line2D
mpl.figure(2)
mpl.title("Average Age per Year Level of Sample Students")
mpl.xlabel("Year Level")
mpl.ylabel("Average Age")

mode_bar_x = np.array([1, 2, 3, 4])
mode_bar_y = np.array(average_ages)
mode_bar = mpl.bar(mode_bar_x, mode_bar_y)
mode_bar[3].set_color('red')
mpl.legend([Line2D([0], [0], color="red", lw=4)],["Mode Average Age"])

mpl.show()
