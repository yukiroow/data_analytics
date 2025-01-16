# Dominguez, Harry
# 9463 - IT 322
# Prelim Activity 1
import pandas as panda
import numpy as numpy

# CLASS.csv
class_data = panda.read_csv("prelimact1/CLASS.csv")

class_means = panda.Series([class_data['quiz 1'].mean(), 
                            class_data['quiz 2'].mean(), 
                            class_data['EXAM'].mean()],
                           index=["Quiz 1 mean score", 
                                  "Quiz 2 mean score", 
                                  "Exam mean score"])

class_medians = panda.Series([class_data['quiz 1'].median(), 
                            class_data['quiz 2'].median(), 
                            class_data['EXAM'].median()],
                             index=["Quiz 1 median score",
                                    "Quiz 2 median score",
                                    "Exam median score"])

class_modes = panda.Series([None if class_data['quiz 1'].size == class_data['quiz 1'].mode().size else class_data['quiz 1'].mode(),
                            None if class_data['quiz 2'].size == class_data['quiz 2'].mode().size else class_data['quiz 2'].mode(),
                            None if class_data['EXAM'].size == class_data['EXAM'].mode().size else class_data['EXAM'].mode()],
                             index=["Quiz 1 mode score",
                                    "Quiz 2 mode score",
                                    "Exam mode score"])