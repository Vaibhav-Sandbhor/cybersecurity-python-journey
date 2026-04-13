# Day 5 - File Handling & Log Analysis (SOC Basics)

## 📚 Topics Covered

* What are Logs in Cybersecurity
* Importance of Logs in SOC
* File Handling in Python
* Reading Files using `with open()`
* Basic Log Analysis (FAILED login detection)

---

## 🧠 SOC Concepts

### 1. What are Logs?

Logs are records of system or user activity.

Example:

```
192.168.1.10 - SUCCESS
192.168.1.20 - FAILED
```

---

### 2. Why Logs are Important in SOC

* Used to detect attacks
* Help in incident investigation
* Provide evidence of system activity

---

### 3. Real-World Example

If multiple failed login attempts are detected:

```
FAILED + multiple attempts → Possible Brute Force Attack
```

---

### 4. Types of Logs (Basic)

* Authentication Logs (login attempts)
* Network Logs (traffic, IP activity)
* System Logs (OS activity)
* Application Logs

---

## 💻 Python Concepts

### 1. File Handling

Used to read and process log files.

---

### 2. Reading a File

```python
with open("log.txt", "r") as file:
    for line in file:
        print(line)
```

---

### 3. Why `with open()` is Used

* Automatically closes the file
* Cleaner and safer approach

---

### 4. Searching in Logs

```python
if "FAILED" in line:
```

Used to detect specific events in logs.

---

## 💻 Practice Code

### Log Analyzer (Basic)

```python
failed_count = 0

with open("log.txt", "r") as file:
    for line in file:
        if "FAILED" in line:
            failed_count += 1

print(f"Failed attempts: {failed_count}")
```

---

### Bonus: Print Only Failed Logs

```python
with open("log.txt", "r") as file:
    for line in file:
        if "FAILED" in line:
            print(line.strip())
```

---

## 🔐 Cybersecurity Connection

* Logs are analyzed in SIEM tools like Splunk
* SOC analysts use logs to detect threats
* This code simulates basic log analysis done in real SOC environments

---

## ⚠️ Mistakes I Fixed

* Learned correct file reading method (`with open`)
* Understood how to search inside logs
* Avoided manual file closing

---

## 🚀 Summary

* Learned how to read files using Python
* Built a basic log analyzer
* Understood how SOC analysts detect failed login attempts
* First step toward building SIEM-like tools
