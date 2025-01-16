# Dominguez, Harry
# 9463 - IT 322
# Prelim Activity 1
import pandas as panda
import numpy as numpy

# SAMPLE.csv
sample_data = panda.read_csv("prelimact1/SAMPLE.csv")

sample_mean = sample_data["AGE"].mean()

sample_median = sample_data["AGE"].median()

sample_mode = sample_data["AGE"].mode()

average_age_year1 = sample_data[sample_data["YEAR"] == 1]["AGE"].mean() # Filter to only 1st years
average_age_year2 = sample_data[sample_data["YEAR"] == 2]["AGE"].mean() # Filter to only 2nd years
average_age_year3 = sample_data[sample_data["YEAR"] == 3]["AGE"].mean() # Filter to only 3rd years
average_age_year4 = sample_data[sample_data["YEAR"] == 4]["AGE"].mean() # Filter to only 4th years

average_ages = panda.Series(
    [average_age_year1, average_age_year2, average_age_year3, average_age_year4]
)

sample_std = average_ages.std(ddof=0) # Population Standard Deviation

sample_var = average_ages.var(ddof=0) # Population Variation

# CLASS.csv
class_data = panda.read_csv("prelimact1/CLASS.csv")

class_means = panda.Series(
    [
        class_data["quiz 1"].mean(),
        class_data["quiz 2"].mean(),
        class_data["EXAM"].mean(),
    ],
    index=["Quiz 1 mean score", "Quiz 2 mean score", "Exam mean score"],
)

class_medians = panda.Series(
    [
        class_data["quiz 1"].median(),
        class_data["quiz 2"].median(),
        class_data["EXAM"].median(),
    ],
    index=["Quiz 1 median score", "Quiz 2 median score", "Exam median score"],
)

class_modes = panda.Series(
    [
        (
            None
            if class_data["quiz 1"].size == class_data["quiz 1"].mode().size
            else class_data["quiz 1"].mode()
        ),
        (
            None
            if class_data["quiz 2"].size == class_data["quiz 2"].mode().size
            else class_data["quiz 2"].mode()
        ),
        (
            None
            if class_data["EXAM"].size == class_data["EXAM"].mode().size
            else class_data["EXAM"].mode()
        ),
    ],
    index=["Quiz 1 mode score", "Quiz 2 mode score", "Exam mode score"],
)

class_vars = panda.Series([class_data["quiz 1"].var(ddof=0), class_data["quiz 2"].var(ddof=0), class_data["EXAM"].var(ddof=0)],
                          index=["Quiz 1 variance", "Quiz 2 variance", "Exam variance"])

class_stds =  panda.Series([class_data["quiz 1"].std(ddof=0), class_data["quiz 2"].std(ddof=0), class_data["EXAM"].std(ddof=0)],
                          index=["Quiz 1 standard deviation", "Quiz 2 standard deviation", "Exam standard deviation"])