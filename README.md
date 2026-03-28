# Book Volume Distribution Problem

## Problem Description

A novel consists of **C** chapters. The task is to split it into **B** volumes (B < C) without rearranging the chapters, so that the **maximum volume thickness** (the sum of pages in each volume) is minimized.

**Constraints:**
- Each chapter starts on a new page
- Chapters cannot be split
- If there are multiple optimal solutions, output any of them

## Input Format
C B
pages[1]
pages[2]
...
pages[C]


- First line: number of chapters **C** and number of volumes **B**  
  (3 ≤ B ≤ 40, B ≤ C ≤ 250, total pages ≤ 3×10⁴)
- Next C lines: number of pages in each chapter

## Output Format
ans
l1 r1
l2 r2
...
lB rB


- First line: minimum possible maximum volume thickness
- Next B lines: start and end chapter indices for each volume (1-indexed)

## Example

**Input:**
5 3
300
300
500
300
300


**Output:**
600
1 2
3 3
4 5


**Explanation:**
- Volume 1: chapters 1-2 (300 + 300 = 600 pages)
- Volume 2: chapter 3 (500 pages)
- Volume 3: chapters 4-5 (300 + 300 = 600 pages)

Maximum volume thickness = 600

## Repository Contents

| File | Algorithm | Description |
|------|----------|-------------|
| `solution_dp_tabular.py` | Dynamic Programming (iterative) | Bottom-up tabular approach |
| `solution_dp_memoization.py` | Dynamic Programming (memoization) | Top-down recursive approach with caching |
| `solution_dp_recursive.py` | Pure Recursion | Simple recursive approach without optimization |

## Algorithm Description

### 1. Dynamic Programming (Tabular) — `solution_dp_tabular.py`

Iterative bottom-up approach. Uses `dp` and `cut` arrays:

- `dp[i][j]` — minimum possible maximum thickness when distributing first `i` chapters into `j` volumes
- `cut[i][j]` — last cut position for reconstructing the answer

**Recurrence Relation:**
dp[i][j] = min_{k = j-1 to i-1} max(dp[k][j-1], sum(pages[k+1..i]))


### 2. Dynamic Programming (Memoization) — `solution_dp_memoization.py`

Top-down recursive approach with results stored in the `dp` array. Combines the clarity of recursion with the efficiency of dynamic programming.

### 3. Pure Recursion — `solution_dp_recursive.py`

Simple recursive implementation without optimization. Computes `f(C, B)` directly using the recurrence relation. May be slow for large inputs but clearly demonstrates the mathematical essence of the solution.

## Complexity

| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Tabular DP | O(C² × B) | O(C × B) |
| Memoization | O(C² × B) | O(C × B) |
| Pure Recursion | O(B × Cᴮ) | O(B) |

## How to Run

```bash
# Any of the three solutions
python solution_dp_tabular.py

# With input redirection from a file
python solution_dp_tabular.py < input.txt
Applications
Optimal distribution of printing jobs

Load balancing in parallel computing

Splitting large datasets for batch processing

Scheduling problems minimizing maximum load

Year
2026
