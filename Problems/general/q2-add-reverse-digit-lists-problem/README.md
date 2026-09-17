# [Q2] Add Reverse-Digit Lists Problem

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=flat-square) ![Category](https://img.shields.io/badge/Category-General-blue?style=flat-square) ![Platform](https://img.shields.io/badge/Platform-SEED--IT-indigo?style=flat-square)

## 📝 Problem Statement

You receive two non-empty linked lists that encode non-negative integers. Each node stores one decimal digit, and the least significant digit appears first. Add the represented integers and output a newly constructed linked list in the same least-significant-digit-first order.

Neither input has a leading zero unless it represents zero itself. Each node value is in [0, 9].

For the supplied JSON interface, each list is written as an array of its node values. As an example, [2,4,3] represents 342. Aim for O(max(n, m)) time and O(1) extra space, excluding the returned list.

## 🧪 Examples

### Example 1

**Input:**
```text
[[2,4,3],[5,6,4]]
```

**Expected Output:**
```text
[7,0,8]
```

**Explanation:** 342 + 465 = 807, represented in reverse order as [7,0,8].

### Example 2

**Input:**
```text
[[0],[0]]
```

**Expected Output:**
```text
[0]
```

**Explanation:** Both lists represent 0. Sum is 0.

### Example 3

**Input:**
```text
[[9,9,9,9,9,9,9],[9,9,9,9]]
```

**Expected Output:**
```text
[8,9,9,9,0,0,0,1]
```

**Explanation:** 9,999,999 + 9,999 = 10,009,998 → reverse digits [8,9,9,9,0,0,0,1].

## 🏷️ Tags

`General` 

---
*Solved on [SEED-IT Platform](https://seed-it.com).*
