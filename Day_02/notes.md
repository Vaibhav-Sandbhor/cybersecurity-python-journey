# Day 2 - Data Types, Loops, and Conditions

## 📚 Topics Covered

* Data Types (int, str, list)
* Lists (storing multiple values)
* for loop (iteration)
* if-elif-else (decision making)
* len() function
* Modulus operator (%)
* "in" keyword

---

## 🧠 Key Concepts

### 1. Data Types

* `int` → Numbers (e.g., 21, 80)
* `str` → Text (e.g., "Vaibhav")
* `list` → Multiple values (e.g., [21, 22, 80, 443])

---

### 2. Lists

* Used to store multiple values in one variable

```python
ports = [21, 22, 80, 443]
```

---

### 3. Loops (for loop)

* Used to iterate over data

```python
for port in ports:
    print(port)
```

---

### 4. Conditions (if-elif-else)

* Used for decision making

```python
if port == 21:
    print("Risky")
elif port in [22, 80]:
    print("Medium")
else:
    print("Safe")
```

---

### 5. len() Function

* Used to get length of string or list

```python
len("Amit")  # Output: 4
```

---

### 6. Modulus Operator (%)

* Used to check remainder

```python
10 % 2 = 0  → Even
15 % 2 = 1  → Odd
```

---

### 7. "in" Keyword

* Used to check multiple values

```python
if port in [21, 23]:
    print("Risky")
```

---

## 💻 Practice Done

### 1. Even/Odd Checker

```python
numbers = [10, 15, 20, 25]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} - Even")
    else:
        print(f"{num} - Odd")
```

---

### 2. Name Filter (Length > 4)

```python
names = ["Vaibhav", "Amit", "Rahul", "Raj"]

for name in names:
    if len(name) > 4:
        print(name)
```

---

### 3. Port Risk Checker

```python
ports = [21, 22, 23, 80, 443]

for port in ports:
    if port in [21, 23]:
        print(f"Risky: {port}")
```

---

## 🔐 Cybersecurity Connection (Basic)

* Ports represent network services
* Some ports are more vulnerable:

  * 21 (FTP) → Risky
  * 22 (SSH) → Medium
  * 443 (HTTPS) → Secure

👉 Learned how to classify ports using logic

---

## ⚠️ Mistakes I Fixed

* Used `==` instead of `>` in length condition
* Improved code readability (variable naming)
* Used `in` instead of multiple `or`

---

## 🚀 Summary

* Learned how to process data using loops
* Applied conditions to filter and classify data
* Built basic logic similar to real-world systems
