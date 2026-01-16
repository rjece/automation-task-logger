# Automation Task Logger

A simple Week 1 automation project that logs tasks into a structured file
so you don’t rely on memory.

This project is intentionally simple and is designed as the **foundation**
for future automation (reminders, decisions, dashboards).

---

## 📁 Project Structure

```
automation-task-logger/
├── src/
│   └── add_task.py        # Script that logs tasks
├── data/
│   └── tasks.csv          # Auto-created task database
├── README.md
└── requirements.txt
```

---

## ⚠️ Important Rule (Read This First)

**Always run the script from the project root folder.**

✔ Correct:

```
automation-task-logger>
```

✘ Wrong:

```
automation-task-logger\src>
```

The script uses relative paths and assumes it is run from the project root.

---

## ▶️ How to Use — Create a Task

### Step 1 — Open PowerShell in the project root

Confirm you are in:

```
automation-task-logger
```

Check by running:

```powershell
cd
```

---

### Step 2 — Run the task logger command

```powershell
python .\src\add_task.py "Task description here" category
```

### Example

```powershell
python .\src\add_task.py "Prepare Node-RED demo" work
```

---

## ✅ What Happens Automatically

When you run the command:

* A file called `data/tasks.csv` is created (if it doesn’t exist)
* The system automatically adds:

  * a unique task ID
  * a timestamp
  * a default status (`pending`)
* The task is saved in a consistent format

No manual formatting. No remembering fields.

---

## 📄 View Logged Tasks

To view all logged tasks:

```powershell
type .\data\tasks.csv
```

---

## 🧪 Expected Output

### Terminal output:

```
Task added: [a1b2c3d4] Prepare Node-RED demo
```

### CSV file content:

```
id,task,category,status,created_at
a1b2c3d4,Prepare Node-RED demo,work,pending,2026-01-16T22:40:12
```

---

## 🧠 Automation Principle

This project automates **memory**, not decisions.

* You no longer rely on remembering tasks
* Every task is captured the same way
* This becomes the foundation for:

  * reminders
  * decision logic
  * dashboards (future weeks)

---

## 📌 Project Status

**Week 1 complete — Task logging automation**
