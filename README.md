# Exam Score Band Counter

## Problem
Given a sorted list of integer exam scores, count how many scores fall within the inclusive range `[low, high]`.

## Approach
Use binary search to find:
1. The first index containing a score greater than or equal to `low`.
2. The first index containing a score greater than `high` (implemented as the first score greater than or equal to `high + 1`, since scores are integers).

The difference between these positions is the answer. This correctly handles duplicates at both boundaries.

## Run
Requires Python 3.

```bash
python main.py
```

Expected output:
```text
6
0
```

## Complexity
- Linear scan: `O(n)` time per query and `O(1)` extra space.
- Binary search solution: `O(log n)` time per query and `O(1)` extra space.
