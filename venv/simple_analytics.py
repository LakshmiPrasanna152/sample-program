# ============================================================
# SIMPLE DATA ANALYTICS - Student Marks Analysis
# Libraries: NumPy, Pandas, Matplotlib
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 50)
print("   SIMPLE DATA ANALYTICS - Student Marks")
print("=" * 50)

# ── 1. CREATE SAMPLE DATA ──────────────────────────────────
data = {
    "Name":    ["Alice", "Bob", "Charlie", "Diana", "Eve",
                "Frank", "Grace", "Hank", "Ivy", "Jack"],
    "Math":    [85, 72, 90, 65, 78, 88, 55, 92, 70, 60],
    "Science": [80, 68, 95, 70, 82, 75, 60, 88, 74, 65],
    "English": [75, 80, 70, 85, 65, 78, 72, 68, 90, 55],
}

df = pd.DataFrame(data)
print("\n📋 Raw Data:\n", df)

# ── 2. NUMPY OPERATIONS ────────────────────────────────────
marks = np.array(df[["Math", "Science", "English"]])

print("\n📊 NumPy Stats:")
print(f"   Overall Mean  : {np.mean(marks):.2f}")
print(f"   Overall Median: {np.median(marks):.2f}")
print(f"   Std Deviation : {np.std(marks):.2f}")
print(f"   Min Score     : {np.min(marks)}")
print(f"   Max Score     : {np.max(marks)}")

# ── 3. PANDAS OPERATIONS ───────────────────────────────────
df["Total"]   = df["Math"] + df["Science"] + df["English"]
df["Average"] = (df["Total"] / 3).round(2)
df["Grade"]   = pd.cut(df["Average"],
                        bins=[0, 60, 70, 80, 90, 100],
                        labels=["F", "D", "C", "B", "A"])

print("\n📈 With Total & Grade:\n", df[["Name","Total","Average","Grade"]])
print("\n📉 Subject-wise Summary:\n", df[["Math","Science","English"]].describe().round(2))

# ── 4. MATPLOTLIB VISUALIZATIONS ──────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Student Marks Analysis", fontsize=16, fontweight="bold")

# Bar Chart – Average marks per student
axes[0].bar(df["Name"], df["Average"], color="steelblue", edgecolor="black")
axes[0].set_title("Average Marks per Student")
axes[0].set_xlabel("Students")
axes[0].set_ylabel("Average")
axes[0].tick_params(axis="x", rotation=45)
axes[0].axhline(df["Average"].mean(), color="red", linestyle="--", label="Mean")
axes[0].legend()

# Pie Chart – Grade distribution
grade_counts = df["Grade"].value_counts()
axes[1].pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%",
            colors=["#4CAF50","#2196F3","#FF9800","#F44336","#9C27B0"])
axes[1].set_title("Grade Distribution")

# Line Chart – Subject-wise scores
for col, color in zip(["Math","Science","English"], ["blue","green","red"]):
    axes[2].plot(df["Name"], df[col], marker="o", label=col, color=color)
axes[2].set_title("Subject-wise Scores")
axes[2].set_xlabel("Students")
axes[2].set_ylabel("Marks")
axes[2].tick_params(axis="x", rotation=45)
axes[2].legend()
axes[2].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("simple_analytics.png", dpi=150, bbox_inches="tight")
print("\n✅ Chart saved: simple_analytics.png")