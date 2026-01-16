import csv
import sys
from datetime import datetime
import uuid
from pathlib import Path

DATA_FILE = Path("data/tasks.csv")

def init_file():
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(exist_ok=True)
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "task", "category", "status", "created_at"])

def add_task(task, category):
    task_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now().isoformat(timespec="seconds")

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([task_id, task, category, "pending", timestamp])

    print(f"Task added: [{task_id}] {task}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python src/add_task.py "task description" category')
        sys.exit(1)

    init_file()
    add_task(sys.argv[1], sys.argv[2])
