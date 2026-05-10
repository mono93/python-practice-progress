# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_numbered_tasks(tasks: list[str]) -> list[str]:
    return_list = []
    for idx, task in enumerate(tasks, start=1):
        return_list.append(f"{idx}. {task}")
    
    return return_list