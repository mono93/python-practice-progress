# This function will be tested automatically. 
# Do not change the function name or parameters.
def mark_completed_tasks(tasks: list[str]) -> list[str]:
    return_list = []
    for _ in tasks:
        return_list.append("Completed: {task}")
    
    return return_list