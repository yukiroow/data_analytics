# Dominguez, Harry
# 9463 - IT 322
# Prelim Activity 1
import pandas as panda

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

class_vars = panda.Series(
    [
        class_data["quiz 1"].var(ddof=0),
        class_data["quiz 2"].var(ddof=0),
        class_data["EXAM"].var(ddof=0),
    ],
    index=["Quiz 1 variance", "Quiz 2 variance", "Exam variance"],
)

class_stds = panda.Series(
    [
        class_data["quiz 1"].std(ddof=0),
        class_data["quiz 2"].std(ddof=0),
        class_data["EXAM"].std(ddof=0),
    ],
    index=[
        "Quiz 1 standard deviation",
        "Quiz 2 standard deviation",
        "Exam standard deviation",
    ],
)

# Display in Tabular Format
from prettytable import PrettyTable

statistical_table = PrettyTable()
statistical_table.title = "CLASS.csv Statistics"
statistical_table.field_names = [
    " ",
    "Mean",
    "Median",
    "Modes",
    "Variance (P)",
    "Standard Deviation (P)",
]
statistical_table.add_rows(
    [
        [
            "Quiz 1",
            class_means["Quiz 1 mean score"],
            class_medians["Quiz 1 median score"],
            class_modes["Quiz 1 mode score"].tolist(),
            class_vars["Quiz 1 variance"],
            class_stds["Quiz 1 standard deviation"],
        ],
        [
            "Quiz 2",
            class_means["Quiz 2 mean score"],
            class_medians["Quiz 2 median score"],
            class_modes["Quiz 2 mode score"],
            class_vars["Quiz 2 variance"],
            class_stds["Quiz 2 standard deviation"],
        ],
        [
            "Exam",
            class_means["Exam mean score"],
            class_medians["Exam median score"],
            class_modes["Exam mode score"],
            class_vars["Exam variance"],
            class_stds["Exam standard deviation"],
        ],
    ]
)
print(statistical_table)
