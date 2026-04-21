import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "History", "Art"]
marks    = [85, 92, 78, 88, 95]

plt.bar(subjects, marks, color="steelblue")
plt.title("Student Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("bar_chart.png", dpi=150)
plt.show()