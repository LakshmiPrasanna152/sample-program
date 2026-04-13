"""
Student Marks Analyzer
Uses: NumPy, numpy.random, Broadcasting
"""
import numpy as np
import numpy.random as npr

# ── STEP 1: Generate Random Student Data ─────────────────
npr.seed(10)

students = ["Alice", "Bob", "Charlie", "Diana", "Evan",
            "Fiona", "George", "Hannah", "Ivan", "Julia"]

subjects = ["Math", "Science", "English", "History", "Computer"]

# Random marks (5 students x 5 subjects), range 40–100
marks = npr.randint(40, 101, size=(10, 5))

print("=" * 55)
print("        STUDENT MARKS TABLE")
print("=" * 55)
print(f"{'Student':<10}", end="")
for s in subjects:
    print(f"{s:>10}", end="")
print(f"{'Total':>8}")
print("-" * 55)

for i, name in enumerate(students):
    print(f"{name:<10}", end="")
    for m in marks[i]:
        print(f"{m:>10}", end="")
    print(f"{marks[i].sum():>8}")

# ── STEP 2: Basic Stats Per Student ──────────────────────
print("\n" + "=" * 55)
print("        STUDENT STATISTICS")
print("=" * 55)
print(f"{'Student':<10} {'Total':>7} {'Avg':>7} {'Max':>7} {'Min':>7} {'Grade':>7}")
print("-" * 55)

totals  = marks.sum(axis=1)      # sum across subjects
avgs    = marks.mean(axis=1)     # mean across subjects
maxs    = marks.max(axis=1)
mins    = marks.min(axis=1)

def grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    else: return "D"

for i, name in enumerate(students):
    g = grade(avgs[i])
    print(f"{name:<10} {totals[i]:>7} {avgs[i]:>7.1f} {maxs[i]:>7} {mins[i]:>7} {g:>7}")

# ── STEP 3: Subject-Wise Stats ────────────────────────────
print("\n" + "=" * 55)
print("        SUBJECT STATISTICS")
print("=" * 55)
print(f"{'Subject':<12} {'Avg':>7} {'Highest':>9} {'Lowest':>8} {'Pass%':>7}")
print("-" * 55)

sub_avg  = marks.mean(axis=0)
sub_max  = marks.max(axis=0)
sub_min  = marks.min(axis=0)
pass_pct = (marks >= 50).sum(axis=0) / len(students) * 100  # broadcasting!

for i, sub in enumerate(subjects):
    print(f"{sub:<12} {sub_avg[i]:>7.1f} {sub_max[i]:>9} {sub_min[i]:>8} {pass_pct[i]:>6.0f}%")

# ── STEP 4: Broadcasting — Normalize Marks (0 to 100) ────
print("\n" + "=" * 55)
print("        NORMALIZED MARKS (0–100 scale)")
print("=" * 55)

col_min = marks.min(axis=0)    # shape (5,)
col_max = marks.max(axis=0)    # shape (5,)

# Broadcasting: (10,5) - (5,) works automatically
normalized = (marks - col_min) / (col_max - col_min) * 100

print(f"{'Student':<10}", end="")
for s in subjects:
    print(f"{s:>10}", end="")
print()
print("-" * 55)
for i, name in enumerate(students):
    print(f"{name:<10}", end="")
    for n in normalized[i]:
        print(f"{n:>9.1f}", end="")
    print()

# ── STEP 5: Top & Bottom Performers ──────────────────────
print("\n" + "=" * 55)
print("        RANKINGS")
print("=" * 55)

ranked = np.argsort(avgs)[::-1]   # descending order
print("Top 3 Students:")
for rank, idx in enumerate(ranked[:3], 1):
    print(f"  {rank}. {students[idx]:<10} Avg: {avgs[idx]:.1f}")

print("\nBottom 3 Students:")
for rank, idx in enumerate(ranked[-3:], 1):
    print(f"  {rank}. {students[idx]:<10} Avg: {avgs[idx]:.1f}")

# ── STEP 6: Class Summary ─────────────────────────────────
print("\n" + "=" * 55)
print("        CLASS SUMMARY")
print("=" * 55)
print(f"  Class Average  : {marks.mean():.2f}")
print(f"  Highest Mark   : {marks.max()}  → {students[np.unravel_index(marks.argmax(), marks.shape)[0]]}")
print(f"  Lowest Mark    : {marks.min()}  → {students[np.unravel_index(marks.argmin(), marks.shape)[0]]}")
print(f"  Overall Pass % : {(marks >= 50).mean() * 100:.1f}%")
print(f"  Std Deviation  : {marks.std():.2f}")
print("=" * 55)