import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

students = pd.read_csv("Students.csv")
print(students.head())      # первые 5
print(students[100:110])      # срез с 100 по 109
print((students.tail()))    # последние 5

with_course = students[students["test preparation course"] == "completed"]
print(with_course[["math score",
                   "reading score",
                   "writing score"]].sort_values(["math score",
                                                  "reading score",
                                                  "writing score"], ascending=False).head())

plt.hist(students["math score"], label="Тест по математике")
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()
