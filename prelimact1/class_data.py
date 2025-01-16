# Dominguez, Harry
# 9463 - IT 322
# Prelim Activity 1
import pandas as panda

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