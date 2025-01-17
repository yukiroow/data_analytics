# Dominguez, Harry
# 9463 - IT 322
# Prelim Activity 1
import pandas as panda
import numpy as np
import matplotlib.pyplot as mpl

class_data = panda.read_csv("prelimact1/CLASS.csv")

student_names = class_data["name"]

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
    "Standard Deviation (P)",
]
statistical_table.add_rows(
    [
        [
            "Quiz 1",
            class_means["Quiz 1 mean score"],
            class_medians["Quiz 1 median score"],
            class_stds["Quiz 1 standard deviation"],
        ],
        [
            "Quiz 2",
            class_means["Quiz 2 mean score"],
            class_medians["Quiz 2 median score"],
            class_stds["Quiz 2 standard deviation"],
        ],
        [
            "Exam",
            class_means["Exam mean score"],
            class_medians["Exam median score"],
            class_stds["Exam standard deviation"],
        ],
    ]
)
print(statistical_table)

# Data Visualization
# Means and Medians
# Quiz 1
first_element = student_names[0]
last_element = student_names[6]

bar_x = np.array(student_names)
bar_y = np.array(class_data["quiz 1"])
median_points_x = [first_element, last_element]
median_points_y = [class_medians["Quiz 1 median score"], class_medians["Quiz 1 median score"]]
mean_points_x = [first_element, last_element]
mean_points_y = [class_means["Quiz 1 mean score"], class_means["Quiz 1 mean score"]]

mpl.figure(1)
mpl.title("Mean and Median Scores of Quiz 1")
mpl.xlabel("Students")
mpl.ylabel("Scores")

mpl.bar(bar_x, bar_y, width=0.3)
mpl.plot(median_points_x, median_points_y, color="red", label="Median Age")
mpl.plot(mean_points_x, mean_points_y, color="yellow", label="Mean Age")

mpl.legend()

# Quiz 2
median_points_y = [class_medians["Quiz 2 median score"], class_medians["Quiz 2 median score"]]
mean_points_y = [class_means["Quiz 2 mean score"], class_means["Quiz 2 mean score"]]
bar_y = np.array(class_data["quiz 2"])
mpl.figure(2)
mpl.title("Mean and Median Scores of Quiz 2")
mpl.xlabel("Students")
mpl.ylabel("Scores")

mpl.bar(bar_x, bar_y, width=0.3)
mpl.plot(median_points_x, median_points_y, color="red", label="Median Age")
mpl.plot(mean_points_x, mean_points_y, color="yellow", label="Mean Age")

mpl.legend()

# Exam
median_points_y = [class_medians["Exam median score"], class_medians["Exam median score"]]
mean_points_y = [class_means["Exam mean score"], class_means["Exam mean score"]]
bar_y = np.array(class_data["EXAM"])
mpl.figure(3)
mpl.title("Mean and Median Scores of Exam")
mpl.xlabel("Students")
mpl.ylabel("Scores")

mpl.bar(bar_x, bar_y, width=0.3)
mpl.plot(median_points_x, median_points_y, color="red", label="Median Age")
mpl.plot(mean_points_x, mean_points_y, color="yellow", label="Mean Age")

mpl.legend()

# Standard Deviation
mpl.figure(4)
std_points_x = ["Quiz 1", "Quiz 2", "Exam"]
std_points_y = np.array(class_stds)

mpl.title("Standard Deviations of each Class Activity")
mpl.xlabel("Activity")
mpl.ylabel("Standard Deviation")
mpl.plot(std_points_x, std_points_y)
mpl.text(std_points_x[0], std_points_y[0], std_points_y[0])
mpl.text(std_points_x[1], std_points_y[1], std_points_y[1])
mpl.text(std_points_x[2], std_points_y[2], std_points_y[2])

mpl.show()
