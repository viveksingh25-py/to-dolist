import argparse
import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path(__file__).with_suffix(".json")


def load_tasks() -> List[Dict[str, str]]:
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks: List[Dict[str, str]]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as handle:
        json.dump(tasks, handle, indent=2, ensure_ascii=False)


def list_tasks(tasks: List[Dict[str, str]]) -> None:
    if not tasks:
        print("No tasks found. Add one with `add`.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task.get("done") else "[ ]"
        print(f"{index}. {status} {task['text']}")


def add_task(tasks: List[Dict[str, str]], text: str) -> None:
    tasks.append({"text": text.strip(), "done": False})
    save_tasks(tasks)
    print(f"Added task: {text}")


def remove_task(tasks: List[Dict[str, str]], task_id: int) -> None:
    if task_id < 1 or task_id > len(tasks):
        print(f"Task {task_id} does not exist.")
        return
    removed = tasks.pop(task_id - 1)
    save_tasks(tasks)
    print(f"Removed task: {removed['text']}")


def mark_task(tasks: List[Dict[str, str]], task_id: int, done: bool) -> None:
    if task_id < 1 or task_id > len(tasks):
        print(f"Task {task_id} does not exist.")
        return
    tasks[task_id - 1]["done"] = done
    save_tasks(tasks)
    state = "completed" if done else "not completed"
    print(f"Marked task {task_id} as {state}.")


def clear_tasks() -> None:
    save_tasks([])
    print("Cleared all tasks.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simple command-line to-do list",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", required=False)

    subparsers.add_parser("list", help="Show current tasks")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("text", nargs="+", help="Text of the task")

    remove_parser = subparsers.add_parser("remove", help="Remove a task by number")
    remove_parser.add_argument("id", type=int, help="Task number to remove")

    done_parser = subparsers.add_parser("done", help="Mark a task as completed")
    done_parser.add_argument("id", type=int, help="Task number to mark done")

    undone_parser = subparsers.add_parser("undone", help="Mark a task as not completed")
    undone_parser.add_argument("id", type=int, help="Task number to mark undone")

    subparsers.add_parser("clear", help="Remove all tasks")

    parser.add_argument(
        "--data-file",
        default=str(DATA_FILE),
        help="Path to the JSON file used for storing tasks",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    global DATA_FILE
    DATA_FILE = Path(args.data_file)

    tasks = load_tasks()
    command = args.command or "list"

    if command == "list":
        list_tasks(tasks)
    elif command == "add":
        add_task(tasks, " ".join(args.text))
    elif command == "remove":
        remove_task(tasks, args.id)
    elif command == "done":
        mark_task(tasks, args.id, True)
    elif command == "undone":
        mark_task(tasks, args.id, False)
    elif command == "clear":
        clear_tasks()
    else:
        list_tasks(tasks)


if __name__ == "__main__":
    main()
