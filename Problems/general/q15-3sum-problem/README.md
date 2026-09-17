# [Q15] 3Sum Problem

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=flat-square) ![Category](https://img.shields.io/badge/Category-General-blue?style=flat-square) ![Platform](https://img.shields.io/badge/Platform-SEED--IT-indigo?style=flat-square)

## 📝 Problem Statement

With an integer array `nums`, output all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

The solution set must not contain duplicate triplets. Each triplet in the returned list should be sorted in non-decreasing order; the judge will normalize and sort the list of triplets before comparison so output ordering is not significant.

Aim for an algorithm that runs in O(n^2) time on average and uses O(1) extra space (excluding the space required for the output). A standard approach is to sort the array and use a two-pointer scan for each fixed first element.

## 🧪 Examples

### Example 1

**Input:**
```text
[[-1,0,1,2,-1,-4]]
```

**Expected Output:**
```text
[[-1,-1,2],[-1,0,1]]
```

**Explanation:** Distinct triplets that sum to zero are [-1,0,1] and [-1,-1,2]. Each triplet is shown in non-decreasing order.

### Example 2

**Input:**
```text
[[0,1,1]]
```

**Expected Output:**
```text
[]
```

**Explanation:** No triplet sums to zero.

### Example 3

**Input:**
```text
[[0,0,0]]
```

**Expected Output:**
```text
[[0,0,0]]
```

**Explanation:** The only triplet [0,0,0] sums to zero.

## 🏷️ Tags

`General` 

---
*Solved on [SEED-IT Platform](https://seed-it.com).*
