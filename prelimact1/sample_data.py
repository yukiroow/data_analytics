# Dominguez, Harry
# 9463 - IT 322
# Prelim Activity 1
import pandas as panda

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