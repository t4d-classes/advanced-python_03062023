def command_show_history(history):
    print(history)

def command_clear_history(history_list):
    # global history
    # history = []
    history_list.clear()

def get_next_id(history):
    next_id = 1
    if history:
        next_id = max([ entry["id"] for entry in history ]) + 1
    return next_id

def command_add_history_entry(history, entry_id, op_name, op_value):
    history.append({
        "id": entry_id,
        "opName": op_name,
        "opValue": op_value
    })

def command_remove_history_entry(history):
    for entry in history:
        if entry["id"] == history_entry_id:
            history.remove(entry)
            break