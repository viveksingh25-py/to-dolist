# To-Do List

A simple command-line to-do list manager written in Python.

## Features

- Add tasks
- List tasks
- Mark tasks as done
- Mark tasks as not done
- Remove tasks
- Clear all tasks
- Persistent storage in a JSON file

## Files

- `to-dolist.py` — main script
- `to-dolist.json` — automatically created storage file for tasks

## Requirements

- Python 3.7+

## Usage

Run the script from the repository folder.

```bash
python to-dolist.py list
python to-dolist.py add "Buy milk"
python to-dolist.py done 1
python to-dolist.py undone 1
python to-dolist.py remove 1
python to-dolist.py clear
```

## Notes

- Tasks are stored in `to-dolist.json` next to `to-dolist.py`.
- If no command is provided, the script shows the task list.

## HTML Version

Open `index.html` in a web browser to use the HTML to-do list interface.

- Type a task into the input field and click `Add` or press Enter.
- Mark tasks done or undo them with the `Done` / `Undo` button.
- Remove tasks with the `Remove` button.
- Use `Clear All` to delete all tasks.
- Tasks are saved automatically in the browser's local storage.
